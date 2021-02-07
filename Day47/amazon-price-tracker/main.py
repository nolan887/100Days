import requests
from bs4 import BeautifulSoup
import smtplib
import os

# -------------------- DEFINE CONSTANTS -------------------- #
amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

my_email = "pythoncraylie@gmail.com"
my_pw = os.environ.get("PYTHON_CRAYLIE_GMAIL_PW")

MM_THRESHOLD = 550.00
MKB_THRESHOLD = 95.00

# -------------------- AMAZON ITEM TRACKING -------------------- #
# Mac Mini M1
mac_mini_url = "https://www.amazon.com/Apple-Mini-Chip-256GB-Storage/dp/B08N5PHB83/"

# Magic Keyboard w/ Numpad
magic_keyboard_url = "https://www.amazon.com/Apple-Keyboard-Numeric-Wireless-Rechargable/dp/B071ZZTNBM"


# -------------------- REQUEST PRICE FROM AMAZON AND CONVERT TO USABLE PYTHON PRICE -------------------- #
# This should be re-written into a function to minimize copy/pasted code
response_mm = requests.get(url=mac_mini_url, headers=amazon_headers)

soup_mini = BeautifulSoup(response_mm.content, "html.parser")

mm_price = soup_mini.find(name="span", id="priceblock_ourprice")
mm_price = mm_price.getText()
mm_price = float(mm_price.split("$")[1])

if mm_price <= MM_THRESHOLD:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: AMAZON PRICE ALERT!\n\n"
                                f"The Mac Mini you were tracking is now below the limit of ${MM_THRESHOLD}" 
                                f" you set and is on sale for ${mm_price}."
                                f"\n\nPurchase now at" 
                                f"{mac_mini_url}".encode("utf-8"))
    print("Mac mini e-mail sent.")
else:
    print(f"Mac Mini is priced at {mm_price}, which is above the set price threshold of {MM_THRESHOLD}")


response_mkb = requests.get(url=magic_keyboard_url, headers=amazon_headers)

soup_magic = BeautifulSoup(response_mkb.content, "html.parser")
mkb_price = soup_magic.find(name="span", id="priceblock_ourprice")
mkb_price = mkb_price.getText()
mkb_price = float(mkb_price.split("$")[1])

if mkb_price <= MKB_THRESHOLD:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: AMAZON PRICE ALERT!\n\n"
                                f"The Magic Keyboard you were tracking is now below the limit of ${MKB_THRESHOLD}" 
                                f" you set and is on sale for ${mkb_price}."
                                f"\n\n Purchase now at" 
                                f" {magic_keyboard_url}".encode("utf-8"))
    print("Magic keyboard e-mail sent.")
else:
    print(f"Magic keyboard is priced at {mkb_price}, which is above the set price threshold of {MKB_THRESHOLD}")

