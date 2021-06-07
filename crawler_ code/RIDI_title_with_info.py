from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re

#자동 로그인
driver = webdriver.Chrome(r'.\chromedriver.exe')
driver.get('https://ridibooks.com/account/login?return_url=https%3A%2F%2Fridibooks.com%2Fromance%2F')
time.sleep(3)

#id/password를 텍스트파일에서 읽어옴
with open('idpass.txt','r',encoding='utf-8') as f:
    idnp=f.readlines()

#id와 password입력
id_input = driver.find_element_by_css_selector('#login_id')
id_input.send_keys(idnp[0])
password_input = driver.find_element_by_css_selector('#login_pw')
password_input.send_keys(idnp[1])

#로그인 버튼 클릭
login_button = driver.find_element_by_css_selector('#login > form > button')
login_button.click()
time.sleep(3)


def crawling_info(infocode):#리뷰 크롤링
        driver.get(infocode)  # 북 코드를 통해 책 구매 페이지로 이동
        time.sleep(3)

        title=[]
        id=[]
        review = []
        rate = []

        # 구매자 리뷰 선택
        b1 = driver.find_element_by_class_name('tab_list')
        b1.click()
        time.sleep(3)

        # 리뷰 끝까지 전부 보기
        while (True):
            try:
                newb = driver.find_element_by_css_selector("#review_list_section > div.review_list_wrapper.js_review_list_wrapper.active > div.more_review_button_wrapper.js_more_review_button_wrapper > button")
                newb.click()
                time.sleep(3)
            except:
                break

        #html가져오기
        source = driver.page_source
        html = bs(source, 'lxml')
        ti= str(html.select_one('h3.info_title_wrap').text)

        # 평점과 리뷰 크롤링
        info = html.select('li.review_list')


        for i in info:
            try:
                title.append(ti)
                id.append(str(i.select_one('span.reviewer_id')).replace('<span class="reviewer_id">', '').replace('</span>', ''))
                st = str(i.select_one('span.StarRate_IconFill'))
                # 5점과 4점은 긍정(1), 3점은 애매모호(0) 1점과 2점은 부정(-1)으로 분류
                if '100%' in st or '80%' in st:
                    r = '1'
                elif '60%' in st:
                    r = '0'
                else:
                    r = '-1'
                # 리스트에 저장
                rate.append(r)
            except:
                    print('')

            try:
                f = str(i)

                if '<span class="hidden">'in f:  #span class="hidden"이 있을 경우
                    ans = re.search(r'<span class="hidden">.+', f).group()
                    t = ans.replace('<span class="hidden">', '').replace('</span></p>', '').replace('<br/>',' ')
                else:     # span class="hidden"이 없을 경우
                    ans = re.search(r'<p class="review_content js_review_content">.+', f).group()
                    t = ans.replace('<p class="review_content js_review_content">', '').replace('</p>', '').replace('<br/>',' ')

                #리스트에 저장
                review.append(t)
            except:
                title.pop()
                id.pop()
                rate.pop()

        data={'title':title,'id':id,'rate':rate,'review':review}
        res = pd.DataFrame(data)



        return res # 반환

#메인
if __name__ == "__main__":
    res = pd.DataFrame(columns=['title','id','rate','review'])

    with open('ridi_code.txt','r',encoding='utf-8') as f:
        c_line=f.readlines()# txt파일에 담긴 책 소개&구매 페이지 주소 가져오기

    for code in c_line:#주소에서 별점과 리뷰 추출
        review = crawling_info(code.replace('\n', '').replace('v2/Detail?id=', 'books/'))
        res = pd.concat([res, review], ignore_index=True,axis=0)
        print(res)

    res.to_csv('ridi_info_with_title_serialization.txt',mode='w' ,sep='\t', index=False)

    print()
    print('=====최종=====')
    print(res)

    # 드라이브 종료
    driver.close()
    driver.quit()

