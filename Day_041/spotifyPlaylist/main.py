from bs4 import BeautifulSoup
import requests
from os import environ
from dotenv import load_dotenv
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import pprint

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
    result = [item for item in sp.search(q=query)[
        "tracks"]["items"] if item["type"] == reqType and item["name"].lower() == name.lower()]
    if (len(result) == 0):
        return f"query: {query} and name: {name} not found"
    return format_spotify_response(result[0])


def main():

    # date = input("Which year would you like to travel? (YYYY-MM-DD): ")
    date = "2000-08-15"
    if (date.count("-") > 3):
        return print("Invalid Date")
    load_dotenv()
    billboard = get_100_billboard(date)[:5]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    songs = [make_spotify_request(sp,  (song["song_name"] + " " +
                                        song["artist_name"]).replace(' ', '+'), "track", song["song_name"]) for song in billboard]
    pprint.pprint(songs)


if __name__ == '__main__':
    main()
