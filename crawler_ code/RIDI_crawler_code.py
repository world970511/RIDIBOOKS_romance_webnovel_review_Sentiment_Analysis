from selenium import webdriver
import time

driver = webdriver.Chrome(r'.\chromedriver.exe')
driver.get('https://ridibooks.com/account/login?return_url=https%3A%2F%2Fridibooks.com%2Fromance%2F')
time.sleep(3)

with open('idpass.txt','r',encoding='utf-8') as f:
    idnp=f.readlines()

id_input = driver.find_element_by_css_selector('#login_id')
id_input.send_keys(idnp[0])
password_input = driver.find_element_by_css_selector('#login_pw')
password_input.send_keys(idnp[1])

login_button = driver.find_element_by_css_selector('#login > form > button')
login_button.click()
time.sleep(3)

driver.get('https://ridibooks.com/keyword-finder/romance?order=review_cnt&page=1&set_id=1')
time.sleep(3)

def craw_code(path,page):
    code = []
    p = 1
    c_button = driver.find_element_by_css_selector(path)
    c_button.click()
    time.sleep(1)

    while(p<page+1):
        l1='https://ridibooks.com/keyword-finder/romance?order=review_cnt&page='
        l2='&set_id=1'

        driver.get(l1 + str(p) + l2)
        time.sleep(3)

        meta = driver.find_elements_by_css_selector("div.RSGBookMetadata")
        for c in meta:
            href=c.find_element_by_tag_name('a').get_attribute('href')
            code.append(href)


        p+=1
    d_button = driver.find_element_by_css_selector('button.Keyword_DeleteButton')
    d_button.click()
    time.sleep(3)

    return code



if __name__ == "__main__":
    with open('ridi_code.txt','w',newline='')as f:
        pagelist=[300,4,35]

        code=[]
        keyword_li=['#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(3) > label',
                '#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(4) > label',
                '#KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(5) > label']

        code += craw_code(keyword_li[0], pagelist[0])
        print(len(code))
        for i in range(1,3):
            code+=craw_code(keyword_li[i],pagelist[i])
            print(len(code))

        f.writelines('\n'.join(code))

        driver.close()








