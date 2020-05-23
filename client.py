import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import RealEstate as re

if __name__ == "__main__":
    re.get_region_list(re.driver)
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