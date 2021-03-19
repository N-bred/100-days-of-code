import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ.get("API_KEY")
API_ENDPOINT = "http://api.openweathermap.org/data/2.5/onecall"

PARAMS = {
    "lat": "4.569951",
    "lon": "-74.100541",
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


def make_request(url, params):
    req = requests.get(url, params)
    req.raise_for_status()
    return req.json()


def main():
    data = make_request(API_ENDPOINT, PARAMS)
    weather_slice = data["hourly"][:12]
    will_rain = False
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if 700 >= int(condition_code) < 800:
            will_rain = True
            break

    if will_rain:
        print("Bring an Umbrella")


if __name__ == "__main__":
    main()
