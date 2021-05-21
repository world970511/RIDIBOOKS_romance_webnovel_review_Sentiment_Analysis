from selenium import webdriver
import time
import csv
import pandas as pd


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

driver.get('https://ridibooks.com/romance/')
time.sleep(3)


def crawling_info(infocode):#리뷰 크롤링
    driver.get(infocode)
    b1 = driver.find_element_by_css_selector('# review_list_section > div.rui_tab_and_order > '
                                                   'ul.rui_tab_2.js_review_list_filter_wrapper > li:nth-child(1) > a')
    b1.click()
    time.sleep(3)

    b2=driver.find_elements_by_css_selector("")
    time.sleep(3)


if __name__ == "__main__":
    df=pd.DataFrame
    with open('ridi_code.txt','r',encoding='utf-8') as f:
        c_line=f.readlines()
    for code in c_line:
        crawling_info(code.replace('\n',''))



    # KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(3) > label > input
   # crawling_info(infocode)
#https://ridibooks.com/keyword-finder/romance?order=recent&page=1&set_id=1

