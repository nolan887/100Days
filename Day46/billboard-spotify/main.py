from bs4 import BeautifulSoup
import requests

songs_list = []

req_date = input("What date do you want to time travel to? (format YYYY-MM-DD): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{req_date}")
song_page = response.text

soup = BeautifulSoup(song_page, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
for song in all_songs:
    song_name = song.getText()
    songs_list.append(song_name)

print(songs_list)