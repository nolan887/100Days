import requests
import os
from twilio.rest import Client

# -------------------- INITIAL SETUP -------------------- #
# SETUP: Stock data fetching
noteworthy_stock_change = 4
stock_direction = None

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_key = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_key,
}

# SETUP: News article fetching
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_key = ""

news_params = {
    "q": STOCK,
    "qInTitle": COMPANY_NAME,
    "apiKey": news_key,
}

# SETUP: Twillio SMS Info
account_sid = "AC96f51ba9845b52998cf4d9fdc593f577"
auth_token = ""



# -------------------- STOCK FETCHING -------------------- #
# Get stock data, look for last two days, determine if a stock has changed > 5%
response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = float(stock_data_list[0]["4. close"])
two_days_ago_closing_price = float(stock_data_list[1]["4. close"])

closing_delta = two_days_ago_closing_price - yesterday_closing_price
if closing_delta > 0:
    stock_direction = "📈"
else:
    stock_direction = "📉"

closing_percent = round((closing_delta / yesterday_closing_price) * 100)

# -------------------- NEWS FETCHING -------------------- #
# Get the latest news, pair down to latest three articles
response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = response.json()["articles"]
top_articles = news_data[:3]
top_articles_info = [f"{STOCK}: {stock_direction}{closing_percent}%\n" \
                     f"Headline: {article['title']}, \n" \
                     f"Brief: {article['description']}" for article in top_articles]

# -------------------- SMS SENDING -------------------- #
client = Client(account_sid, auth_token)
if abs(closing_percent) > noteworthy_stock_change:
    for article in top_articles_info:
        print(article)
        # message = client.messages.create(
        #     body=article,
        #     from_='+16692013335',
        #     to='+14016225183'
        # )
else:
    print("Nothing newsworthy")
