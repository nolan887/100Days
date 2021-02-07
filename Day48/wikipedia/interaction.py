from selenium import webdriver

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

wiki_home_url = "https://en.wikipedia.org/wiki/Main_Page"

target_url = wiki_home_url
driver.get(target_url)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

driver.quit()




