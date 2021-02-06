from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")

songs_list = []
songs_uris = []

# --------------- SPOTIFY SETUP --------------- #
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# --------------- USER INPUT DATE FOR BILLBOARD --------------- #
req_date = input("What date do you want to time travel to? (format YYYY-MM-DD): ")
year = req_date.split("-")[0]


# --------------- BILLBOARD TOP 100 SONG LIST GENERATION --------------- #
response = requests.get(f"https://www.billboard.com/charts/hot-100/{req_date}")
song_page = response.text

soup = BeautifulSoup(song_page, "html.parser")

all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
for song in all_songs:
    song_name = song.getText()
    songs_list.append(song_name)


# --------------- SEARCH FOR SONGS AND GENERATE SPOTIFY PLAYLIST --------------- #
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"Billboard Top 100 for Week of {req_date}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)

