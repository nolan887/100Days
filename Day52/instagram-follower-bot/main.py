import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# -------------------- INSTAGRAM SETUP -------------------- #
insta_user = "cloudbreakdev@gmail.com"
insta_pass = os.environ.get("CLOUDBREAK_INSTAGRAM_PW")


# -------------------- WEB DRIVER SETUP -------------------- #
chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
login_page_url = "https://www.instagram.com/"

# -------------------- WEB DRIVER ACTION -------------------- #
# Log into Instagram
target_url = login_page_url
driver.get(target_url)

login_field = driver.find_element_by_name("username")
pw_field = driver.find_element_by_name("password")

login_field.send_keys(insta_user)
pw_field.send_keys(insta_pass)
pw_field.send_keys(Keys.ENTER)
print("Logged in.")