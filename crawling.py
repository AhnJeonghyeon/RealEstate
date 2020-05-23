import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


def search_instagram(word):
    path = "https://www.instagram.com/explore/tags/"+word
    return path

def search_first(driver):
    browser = driver.Chrome('/Users/AhnJeongHyeon/Downloads/데이터마이닝/chromedriver')
    browser.get(search_instagram('제주도'))
    return


if __name__ == "__main__":
    driver = webdriver
    search_first(driver)
    time.sleep(3)
    
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