from bs4 import BeautifulSoup
import requests

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


def main():
    date = input("Which year would you like to travel? (YYYY-MM-DD): ")
    if (date.count("-") > 3):
        return print("Invalid Date")
    billboard = get_100_billboard(date)
    print(billboard)


if __name__ == '__main__':
    main()
