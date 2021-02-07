import requests
from bs4 import BeautifulSoup

# -------------------- DEFINE CONSTANTS -------------------- #
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


# -------------------- AMAZON ITEM TRACKING -------------------- #
# Mac Mini M1
amazon_item_url = "https://www.amazon.com/Apple-Mini-Chip-256GB-Storage/dp/B08N5PHB83/"

# Magic Keyboard w/ Numpad
# amazon_item_url = "https://www.amazon.com/Apple-Keyboard-Numeric-Wireless-Rechargable/dp/B071ZZTNBM"


# -------------------- REQUEST PRICE FROM AMAZON AND CONVERT TO USABLE PYTHON PRICE -------------------- #
response = requests.get(url=amazon_item_url, headers=amazon_headers)

soup = BeautifulSoup(response.content, "html.parser")

item_price = soup.find(name="span", id="priceblock_ourprice")
item_price = item_price.getText()
item_price = float(item_price.split("$")[1])
print(item_price)