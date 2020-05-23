import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
driver = webdriver

def get_path():
    path = "http://www.rtech.or.kr/rtech/main/mapSearch.do?popUpYn=&posX=37.48027664277273&posY=127.06259255237846"
    return path


def start_driver(driver):
    driver = driver.Chrome('/Users/AhnJeongHyeon/Downloads/데이터마이닝/부동산/chromedriver')
    driver.get(get_path())
    return driver

def get_region_list(driver):
    #list를 입력받고 do_code1, ..에서 확인하고 없으면 짤
    address = input("주소를 입력해주세요")
    address_list = address.split(" ")
    #send_keys로 값 할당
    city = driver.find_element_by_id("do_code1")
    city.send_keys(str(address_list[0]))
    do = driver.find_element_by_id("city_code1")
    do.send_keys(str(address_list[1]))
    '''
    dong = driver.find_element_by_id("dong_code1")
    dong.send_keys(str(address_list[2]))
    '''
    search = driver.find_element_by_class_name("map_search_inputtxt2_search2")
    search.click()
    # address에 입력한대로 주소를 입력하고 파라미터를 이용해 click함수 발생

    html = driver.page_source
    soup = bs(html, 'html.parser')
    #그다음 옆에 뜨는 li 가져와서 출력
    #soup.select는 class와 id정보를 가져오는 함수이다 #이면 id, .이면 class를 가져온다
    li = soup.select("#aptListArea>li")# > 로 아래 하위 css를 가져올 수 있다.
    print(li)
    #TODO split 해서 DF에 넣어보자
    temp = []
    temp = str(li).split('<li>')
    list = []
    for i in range(0,len(temp)):
        if len(temp[i]) > 10:
            list.append(temp[i])
    #<a href="javascript:go_apt_info(\'1\',\'2559\',\'1135010600\');">
        # <span class="map_right_con1">
            # 아
        # </span>
        # 건영2
        # <span>
            # (6동                    742세대 )
        # </span>
    # </a>
# </li>,
    #<가 시작하면 다 skip, >가 나오고나면 append 시작
    last = []
    for i in range(0,len(list)):
        t = []
        check = False
        string = ""
        for j in range(0, len(list[i])):
            if list[i][j] == '<':
                check = False
                if string != "":
                    t.append(string)
                string = ""
            elif list[i][j] == '>':
                check = True
            else:
                if check:
                    string += list[i][j]
        last.append(t)
    print(last)
    #return df

if __name__ == "__main__":

    driver = start_driver(driver)
    get_region_list(driver)

    '''
    options = Options()
    options.headless = True
    #browser = webdriver.Chrome(executable_path="/Users/AhnJeongHyeon/Downloads/chromedriver", options=options)
    browser = webdriver.Chrome('/Users/AhnJeongHyeon/Downloads/데이터마이닝/chromedriver')
    browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

    time.sleep(3)
    tag_names = browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
    for tag in tag_names:
        print(tag.text.split("\n"))

    '''