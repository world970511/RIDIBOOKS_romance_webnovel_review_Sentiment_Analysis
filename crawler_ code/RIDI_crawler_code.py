from selenium import webdriver
import time

#메인 홈페이지에서 자동 로그인
driver = webdriver.Chrome(r'.\chromedriver.exe')
driver.get('https://ridibooks.com/account/login?return_url=https%3A%2F%2Fridibooks.com%2Fromance%2F')
time.sleep(3)

#id/password가 담긴 텍스트 파일에서 id와 password를 읽어내어 자동 로그인
with open('idpass.txt','r',encoding='utf-8') as f:
    idnp=f.readlines()

id_input = driver.find_element_by_css_selector('#login_id')
id_input.send_keys(idnp[0])
password_input = driver.find_element_by_css_selector('#login_pw')
password_input.send_keys(idnp[1])

#로그인 확인 버튼 클릭
login_button = driver.find_element_by_css_selector('#login > form > button')
login_button.click()
time.sleep(3)

#키워드로 찾기 페이지로 이동
driver.get('https://ridibooks.com/keyword-finder/romance?order=review_cnt&page=1&set_id=1')
time.sleep(3)

def craw_code(path,page):
    code = []
    p = 1

    #키워드 입력
    c_button = driver.find_element_by_css_selector(path)
    c_button.click()
    time.sleep(1)

    while(p<page+1):
        l1='https://ridibooks.com/keyword-finder/romance?order=review_cnt&page='
        l2='&set_id=1'

        #다음 페이지로 이동
        driver.get(l1 + str(p) + l2)
        time.sleep(3)

        #북 코드 추출
        meta = driver.find_elements_by_css_selector("div.RSGBookMetadata")
        for c in meta:
            href=c.find_element_by_tag_name('a').get_attribute('href')
            code.append(href)
        p+=1


    #이전 키워드 취소
    d_button = driver.find_element_by_css_selector('button.Keyword_DeleteButton')
    d_button.click()
    time.sleep(3)

    return code



if __name__ == "__main__":
    with open('ridi_code.txt','w',newline='')as f:
        pagelist=[300,4,35]

        code=[]

        #키워드- 단행본/연재중/연재완료 중 하나가 들어간 로맨스 소설 북코드 추출
        keyword_li=['#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(3) > label',
                '#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(4) > label',
                '#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(5) > label']

        code += craw_code(keyword_li[0], pagelist[0])
        print(len(code))        #뽑아온 리스트 크기를 통해 몇개가 추출되었는지 확인

        for i in range(1,3):
            code+=craw_code(keyword_li[i],pagelist[i])
            print(len(code))        #뽑아온 리스트 크기를 통해 몇개가 추출되었는지 확인

        f.writelines('\n'.join(code))#txt파일에 쓰기

        driver.close()
