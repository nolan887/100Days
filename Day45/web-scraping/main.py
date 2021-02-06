from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# Some websites will need lxml to be used as the parser in the code above

print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print(soup)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

# Selector follows the same format as CSS the below line looks for the first URL it comes across that is <a> inside of a <p>
company_url = soup.select_one(selector="p a")
print(company_url)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)