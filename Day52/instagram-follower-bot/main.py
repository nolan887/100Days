import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException



insta_user = "cloudbreakdev@gmail.com"
insta_pass = os.environ.get("CLOUDBREAK_INSTAGRAM_PW")
similar_account = "pmi_org"
similar_account2 = "smallbusinesstips_"
chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
login_page_url = "https://www.instagram.com/accounts/login/"



class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get(login_page_url)
        time.sleep(3)

        login_field = self.driver.find_element_by_name("username")
        login_field.send_keys(insta_user)

        pw_field = self.driver.find_element_by_name("password")
        pw_field.send_keys(insta_pass)

        time.sleep(2)
        pw_field.send_keys(Keys.ENTER)

    def find_followers(self, to_follow):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{to_follow}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers(similar_account)
bot.follow()
bot.find_followers(similar_account2)
bot.follow()
