from selenium import webdriver

cookie_monster_is_chomping = True

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


target_url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(target_url)

big_cookie = driver.find_element_by_id("bigCookie")

while cookie_monster_is_chomping:
    big_cookie.click()

driver.quit()