from bs4 import BeautifulSoup
import requests

movie_count = 0

response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h1", class_="list-item__title")

with open("movie_list.txt", mode="a") as file:
    for movie in reversed(all_movies):
        movie_count += 1
        movie_name = movie.getText()
        file.write(f"\n{movie_count}) {movie_name}")
