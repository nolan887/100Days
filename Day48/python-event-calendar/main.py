from selenium import webdriver

events = {}

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

python_url = "https://www.python.org/"

target_url = python_url
driver.get(target_url)

dates = driver.find_elements_by_css_selector(".event-widget time")
descr = driver.find_elements_by_css_selector(".event-widget li a")

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": descr[n].text,
    }

print(events)

driver.quit()

