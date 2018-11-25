from selenium import webdriver
import pandas
from config import SELENIUM_CONFIG ## for config

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


# example two -> crawling TripAdvisor


"""
    parse tripadvisor and save data as Excel!

"""
province_url = "https://www.tripadvisor.com/Restaurant_Review-g32655-d594024-Reviews-Providence-Los_Angeles_California.html"
driver.get(province_url)
CSS_review = "div.review"
reviews = driver.find_elements_by_css_selector(CSS_review)
len(reviews)
CSS_review_title = "div.quote a"
for review in reviews:
    title = review.find_element_by_css_selector(CSS_review_title)
    print(title.text)
data = pandas.DataFrame()
def find_title(review):
    title = review.find_element_by_css_selector(CSS_review_title)
    return title.text

data['title'] = list(map(find_title, reviews))

def find_review_anchor(review):
    review_title = review.find_element_by_css_selector(CSS_review_title)
    return review_title.get_attribute("href")
data['review_url'] = list(map(find_review_anchor, reviews))

CSS_review_content = "div.prw_reviews_text_summary_hsx"
def find_review_content(review):
    content = review.find_element_by_css_selector(CSS_review_content)
    return content.text
data['review_content'] = list(map(find_review_content, reviews))

data.to_excel("example.xls")

driver.close()