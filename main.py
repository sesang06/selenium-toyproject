from selenium import webdriver
import pandas
import time
from konlpy.tag import Twitter
from config import SELENIUM_CONFIG ## for config
from selenium.webdriver.common.keys import  Keys

driver = webdriver.Chrome(SELENIUM_CONFIG['chrome_driver_path'])

#
# driver.get('https://www.naver.com')
# driver.implicitly_wait(3)
# driver.find_element_by_class_name('lg_local_btn').click()
# driver.find_element_by_name('id').send_keys('aaa')
# driver.find_element_by_name('pw').send_keys('aaa')
# driver.implicitly_wait(3)
#
# # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# driver.find_element_by_class_name('btn_global').click()


# # example two -> crawling TripAdvisor
#
#
# """
#     parse tripadvisor and save data as Excel!
#
# """
# province_url = "https://www.tripadvisor.com/Restaurant_Review-g32655-d594024-Reviews-Providence-Los_Angeles_California.html"
# driver.get(province_url)
# CSS_review = "div.review"
# reviews = driver.find_elements_by_css_selector(CSS_review)
# len(reviews)
# CSS_review_title = "div.quote a"
# for review in reviews:
#     title = review.find_element_by_css_selector(CSS_review_title)
#     print(title.text)
# data = pandas.DataFrame()
# def find_title(review):
#     title = review.find_element_by_css_selector(CSS_review_title)
#     return title.text
#
# data['title'] = list(map(find_title, reviews))
#
# def find_review_anchor(review):
#     review_title = review.find_element_by_css_selector(CSS_review_title)
#     return review_title.get_attribute("href")
# data['review_url'] = list(map(find_review_anchor, reviews))
#
# CSS_review_content = "div.prw_reviews_text_summary_hsx"
# def find_review_content(review):
#     content = review.find_element_by_css_selector(CSS_review_content)
#     return content.text
# data['review_content'] = list(map(find_review_content, reviews))
#
# data.to_excel("example.xls")




url = "https://www.instagram.com/explore/tags/python"

driver.get(url)
totalCount = driver.find_element_by_class_name('g47SY').text
print("total ", totalCount)

elem = driver.find_element_by_tag_name("body")
alt_lst = []
pagedowns = 1

while pagedowns < 20:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    img = driver.find_elements_by_css_selector('div.KL4Bh > img')
    for i in img:
        alt_lst.append(i.get_attribute('alt'))
    pagedowns += 1

alt_lst = list(set(alt_lst))

dic_data = {}

tw = Twitter()

for alt in alt_lst:
    temp = tw.pos(alt, norm = True)
    for data in temp:
        if data[1] == "Hashtag":
            if not (data[0] in dic_data):
                dic_data[data[0]] = 0
            dic_data[data[0]] += 1

keys = sorted(dic_data.items(), key = lambda x:x[1], reverse= True)

for k, v in keys[:15]:
    print("{}({})".format(k,v))
driver.close()