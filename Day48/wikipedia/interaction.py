from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
lab_test_url = "http://secure-retreat-92358.herokuapp.com/"

# wiki_home_url = "https://en.wikipedia.org/wiki/Main_Page"

# target_url = wiki_home_url
target_url = lab_test_url
driver.get(target_url)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Tom Brady")
# search.send_keys(Keys.ENTER)

# driver.quit()

first = driver.find_element_by_name("fName")
last = driver.find_element_by_name("lName")
contact = driver.find_element_by_name("email")

first.send_keys("Charlie")
last.send_keys("Nolan")
contact.send_keys("pythoncraylie@gmail.com")
# contact.send_keys(Keys.ENTER)

submit = driver.find_element_by_css_selector("form button")
submit.click()

