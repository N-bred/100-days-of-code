from bs4 import BeautifulSoup
import requests
from os import environ
from dotenv import load_dotenv
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth


scope = "playlist-modify-private"
URL = "https://www.billboard.com/charts/hot-100/"


def make_request(url, params={}):
    req = requests.get(url, params)
    req.raise_for_status()
    res = req.text
    return res


def parse_text(text: BeautifulSoup):
    song_name = text.find(
        "span", class_="chart-element__information__song").get_text()
    artist_name = text.find(
        "span", class_="chart-element__information__artist").get_text()
    return {"song_name": song_name, "artist_name": artist_name}


def get_100_billboard(date):
    request = make_request(URL + date)
    beautifulSoup = BeautifulSoup(request, features="lxml")
    chart_list = beautifulSoup.find("div", class_="chart-list container")
    return [parse_text(data) for data in chart_list.find_all(
        "span", class_="chart-element__information")]


def format_spotify_response(item):
    return {
        "id": item['id'],
        "name": item["name"],
        "href": item["href"],
        "uri": item["uri"],
        "preview_url": item["preview_url"],
        "artists": [{"artist_name": i["name"], "artist_url": i["href"]} for i in item["artists"]],
        "album": item["album"]["name"],
        "images": [image for image in item["album"]["images"]]
    }


def make_spotify_request(sp: Spotify, query, reqType, name):
    result = None
    request = sp.search(q=query)["tracks"]["items"]
    if len(request) == 0:
        return
    for item in request:
        if item["type"] == reqType and item["name"].lower() == name.lower():
            result = format_spotify_response(item)
    return result


def main():
    date = input("Which year would you like to travel? (YYYY-MM-DD): ")
    if (date.count("-") > 3):
        return print("Invalid Date")
    load_dotenv()
    billboard = get_100_billboard(date)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    songs = [make_spotify_request(sp,  (song["song_name"] + " " +
                                        song["artist_name"]).replace(' ', '+'), "track", song["song_name"]) for song in billboard]

    playlist = sp.user_playlist_create(
        environ["SPOTIFY_USER_ID"], f"{date} Billboard 100", False, description=f"Playlist with the top 100 songs from {date}")

    sp.user_playlist_add_tracks(environ["SPOTIFY_USER_ID"], playlist["id"], [
                                song["uri"] for song in songs if song is not None])


if __name__ == '__main__':
    main()
