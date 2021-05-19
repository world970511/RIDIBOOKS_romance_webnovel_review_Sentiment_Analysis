from selenium import webdriver
import time
import requests
from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup as bs
import pandas as pd


def need_id(info_code):#로그인이 필요할 경우 로그인하여 리뷰 크롤링
    driver = webdriver.Chrome(r'.\chromedriver.exe')
    driver.get(info_code)
    time.sleep(3)

    with open('idpass.txt','r',encoding='utf-8') as f:
        idnp=f.readlines()

    id_input = driver.find_element_by_css_selector('#login_id')
    id_input.send_keys(idnp[0])
    password_input = driver.find_element_by_css_selector('#login_pw')
    password_input.send_keys(idnp[1])

    login_button = driver.find_element_by_css_selector('#login > form > button')
    login_button.click()


def crawling_info():#리뷰 크롤링
    info_html='https://ridibooks.com/books/'
    for code in infocode:
        info=info_html+str(code)
        try:
            print("제작중")
        except:
            need_id(info)


if __name__ == "__main__":
    infocode=[]#웹소설 등록 코드 추출
    link='https://ridibooks.com/keyword-finder/romance?order=recent&page=1&set_id=1'
    r = requests.get(link)
    soup = bs(r, 'html.parser')
    l = soup.find_all("a")

    # KeywordFinderRenewal > div.KeywordGroup > fieldset:nth-child(6) > div > div > div:nth-child(1) > ul > li:nth-child(3) > label > input
   # crawling_info(infocode)
#https://ridibooks.com/keyword-finder/romance?order=recent&page=1&set_id=1

