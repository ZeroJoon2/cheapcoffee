import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import requests
from bs4 import BeautifulSoup

import pandas as pd

## 전역 변수
search_list = ['서울','경기','인천','강원','광주','대전','대구','부산','울산','세종','경남','경북','전남','전북','충남','충북', '제주']
francise_list = []


# ***********************************************************
# ***********************************************************
# *****************셀레니움***********************************
# ***********************************************************
# ***********************************************************
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.mega-mgccoffee.com/store/find/')

print('창 염')


for i in search_list:
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.ID, 'store_search'))

    )

    print('찾음')
    # 지역 검색 클릭
    #선택자 : body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li.check
    element_location = driver.find_element(by = By.ID, value = 'store_search')
    element_location.send_keys(i)

    #검색 버튼 클릭
    driver.find_element(by = By.ID, value = 'search_map').click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'li'))
    )

    #너무 빨라서 5초 쉼
    time.sleep(5)
    print('검색 조회 다 기다림')

    mega_html = driver.page_source

    # ***********************************************************
    # ***********************************************************
    # **********************BeautifulSoup************************
    # ***********************************************************
    # ***********************************************************
    soup = BeautifulSoup(mega_html, 'html.parser')

    for i in soup.select('#store_search_list a'):
        #지점명
        for j in i.select('.cont_text_inner b'):
            tmp1 = j.text

        #주소 및 전화번호
        for j in i.select('.cont_text_info'):
            tmp2 = j.text.strip().replace('\t\t\t\t\t\t\t','\n').split('\n')

        francise_list.append([tmp1, tmp2[0], tmp2[-1]])

    # 새로고침해서 지역 검색 반복
    driver.refresh()

print(francise_list)

df = pd.DataFrame(francise_list, columns=['francise_name', 'address', 'TEL'])
df.to_csv('mega.csv', index=True, encoding='cp949')
