import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth



user_input = input("Which year do you want to travel to type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/2011-11-09/")
response.raise_for_status()
webpage = response.text

# getting the songs of the date
soup = BeautifulSoup(webpage, "html.parser")
song_name = [item.getText().strip() for item in soup.select(selector="li h3", id="title-of-a-story",)]
#print(song_name)

# spotify
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
# print(CLIENT_ID)
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# print(CLIENT_SECRET)
REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
results = sp.current_user()['id']

song_uri = []
for item in song_name:
    search = sp.search(q=f"track:{item} year:{int(user_input.split('-')[0])}", type='track')
    try:
        song_uri.append(search["tracks"]["items"][0]["uri"])
    except IndexError:
        continue
playlist = sp.user_playlist_create(user=results, name=f'{user_input} BillBoard 100', public=False,
                                   description='created playlist using webscraping')

# adding songs to new playlist
sp.playlist_add_items(playlist_id=playlist['id'],items=song_uri)