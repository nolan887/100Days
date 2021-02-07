from selenium import webdriver

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

mac_mini_url = "https://www.amazon.com/Apple-Mini-Chip-256GB-Storage/dp/B08N5PHB83/"
python_url = "https://www.python.org/"

# target_url = mac_mini_url
target_url = python_url

driver.get(target_url)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)


driver.quit()