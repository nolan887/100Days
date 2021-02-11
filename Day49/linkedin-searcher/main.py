import os
import time
from selenium import webdriver


# -------------------- LINKEDIN SETUP -------------------- #
linkedin_user = "cloudbreakdev@gmail.com"
linkedin_pass = os.environ.get("CLOUDBREAK_LINKEDIN_PW")


# -------------------- WEB DRIVER SETUP -------------------- #
chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
login_page_url = "https://www.linkedin.com/"
jobs_page_url = "https://www.linkedin.com/jobs/search/?f_CF=f_WRA&f_CR=103644278&f_E=2&f_JT=F%2CC&f_LF=f_AL&f_TPR=r2592000&geoId=92000000&keywords=python%20developer&location=Worldwide"

# -------------------- WEB DRIVER ACTION -------------------- #
# Log into Linkedin
target_url = login_page_url
driver.get(target_url)

login_field = driver.find_element_by_name("session_key")
pw_field = driver.find_element_by_name("session_password")
sign_in_button = driver.find_element_by_class_name("sign-in-form__submit-button")

login_field.send_keys(linkedin_user)
pw_field.send_keys(linkedin_pass)
sign_in_button.click()
print("Logged in. Waiting for page load to continue to job search.")

# Wait to ensure login is complete
time.sleep(5)

# Go to jobs page
target_url = jobs_page_url
driver.get(target_url)
print("Job search page launched, looking for job postings.")

count = 1

while count <= 11:
    next_posting = driver.find_element_by_xpath(f"/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[{count}]/div/div")
    print(f"Found job: \n{next_posting.text}")
    next_posting.click()
    time.sleep(3)

    save_button = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/button")
    save_button.click()
    print(f"Saved job #{count - 1}.")

    count += 1

# -------------------- WEB DRIVER COMPLETE -------------------- #
driver.quit()
