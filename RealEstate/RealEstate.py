import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import numpy as np
import time
import AnalysisModule



def get_path():
    path = "http://www.rtech.or.kr/rtech/main/mapSearch.do?popUpYn=&posX=37.48027664277273&posY=127.06259255237846"
    return path


def start_driver(driver):
    driver = driver.Chrome('/Users/AhnJeongHyeon/Documents/GitHub/RealEstate/chromedriver')
    driver.get(get_path())
    return driver


def get_region_list(driver):
    # list를 입력받고 do_code1, ..에서 확인하고 없으면 짤
    address = input("주소를 입력해주세요")
    address_list = address.split(" ")
    # send_keys로 값 할당
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
    # 그다음 옆에 뜨는 li 가져와서 출력
    # soup.select는 class와 id정보를 가져오는 함수이다 #이면 id, .이면 class를 가져온다
    li = soup.select("#aptListArea>li")  # > 로 아래 하위 css를 가져올 수 있다.

    # TODO split 해서 DF에 넣어보자
    temp = []
    temp = str(li).split('<li>')
    list = []
    for i in range(0, len(temp)):
        if len(temp[i]) > 10:
            list.append(temp[i])
            # <a href="javascript:go_apt_info(\'1\',\'2559\',\'1135010600\');">
            # <span class="map_right_con1">
            # 아
            # </span>
            # 건영2
            # <span>
            # (6동                    742세대 )
            # </span>
            # </a>
            # </li>,
    # <가 시작하면 다 skip, >가 나오고나면 append 시작
    last = []
    for i in range(0, len(list)):
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
    return last


def get_df(list):
    column = ['HousingType', 'HousingNm', 'HousingInfo']
    # df = pd.DataFrame(pd.Series([1,2,3], index=column),columns=column)
    S_list = []
    for i in range(0, len(list)):
        S_list.append(pd.Series(list[i], index=column))
    df = pd.DataFrame(S_list)
    #dataframe append series
    return df


def get_Housing_Info(df, index, driver):
    index = int(index)
    print(df.iloc[index, :])        #index로 접근하려면 iloc
    #df에서 선택한 index로 click이벤트 누르고 그 페이지에 있는
    #주소, 면적별 시세, 세대수, 하한/상한 평균가, 전용면적, 전월세 비용)
    # 1/3년 시세추이 가져옴
    driver.find_element_by_css_selector("#aptListArea > li:nth-of-type("+str(index)+") > a").click()
    #NOTE css로 ul을 찾은 다음 li선택 click
    time.sleep(3)
    print(driver.window_handles)
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    #NOTE
    html = driver.page_source
    soup = bs(html, 'html.parser')
    print(soup)
    title = soup.select("#aptName")
    print(title)
    #TODO 집값 데이터 가져오기.




def main_flow(d):
    driver = start_driver(d)
    while 1:
        print("원하는 기능을 선택해주세요")
        select = input("1.지역검색 2.지역최고(저)상승아파트 3.SNS여론검색 4.분양가검색 5.종료")
        if select == '1':
            region_list = get_region_list(driver)
            df = get_df(region_list)
            print(df)
            choose = input("상세정보를 확인하시겠습니까?(Y/N)")
            if choose == 'Y':
                print("번호를 입력해주세요")
                index = input()
                get_Housing_Info(df, index, driver)
        elif select == '2':
            #그 지역 최고가, 최저가 가져오기
            AnalysisModule.getBigGap()
            #TODO 예측값 가져오기
            #TODO 가장 많이 오른 지역
        elif select == '3':
            print()
        elif select == '4':
            print()
        elif select == '5':
            break
        

if __name__ == "__main__":
    d = webdriver
    main_flow(d)
