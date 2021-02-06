from bs4 import BeautifulSoup
import requests

article_texts = []
article_links = []

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title.getText())

articles = soup.find_all(name="a", class_="storylink")

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# This finds all of the scores and adds them to a list, but we can't use .getText() on a list
# article_upvote = soup.find_all(name="span", class_="score")

# So we use list comprehension -- which gives us the string "41 points"
# article_upvote = [score.getText() for score in soup.find_all(name="span", class_="score")]

# So we modify to return the integer only
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])