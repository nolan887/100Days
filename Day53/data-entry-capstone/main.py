import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# -------------------- CONSTANTS -------------------- #
GOOGLE_FORM_URL = "https://forms.gle/ogz67dkmnbh7TgG67"
ZILLOW_SEARCH_URL = "https://www.zillow.com/homes/for_rent/2-_beds/1.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22westerly%2C%20ri%22%2C%22mapBounds%22%3A%7B%22west%22%3A-71.9917623347168%2C%22east%22%3A-71.79091852368164%2C%22south%22%3A41.308416843468414%2C%22north%22%3A41.4013208966447%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"
ZILLOW_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
chrome_driver_path = "/Users/charlesnolan/python/chromedriver"

# -------------------- Scrape Zillow with Beautiful Soup -------------------- #

response = requests.get(url=ZILLOW_SEARCH_URL, headers=ZILLOW_HEADERS)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")

addresses = soup.select(".list-card-addr")
all_addresses = [rental.get_text() for rental in addresses]
print("Addresses retrieved.")

prices = soup.select(".list-card-price")
all_prices = [rental.get_text() for rental in prices]
print("Prices retrieved.")

descriptions = soup.select(".list-card-details")
all_descriptions = [rental.get_text() for rental in descriptions]
print("Descriptions retrieved.")

links = soup.select(".list-card-info a")
all_links = []
for link in links:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
print("Links retrieved.")

# -------------------- Use Selenium to input scraped data via Google Form -------------------- #
print("Launching Google Form.")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for rental in range(len(all_links)):
    time.sleep(2)
    driver.get(GOOGLE_FORM_URL)
    addr_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    descr_field = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span")
    addr_field.send_keys(all_addresses[rental])
    price_field.send_keys(all_prices[rental])
    link_field.send_keys(all_links[rental])
    descr_field.send_keys(all_descriptions[rental])
    submit_button.click()
    print("Rental added.")

print("Form submission complete, shutting down.")
driver.quit()