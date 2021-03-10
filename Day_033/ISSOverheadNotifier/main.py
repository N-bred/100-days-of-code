from requests import get
from datetime import datetime
from time import sleep
from smtpHandler import SmtpHandler

MY_LAT = 51.507351
MY_LONG = -0.127758
HOST = "smtp.google.com"
PORT = 567
USER = "dummyemail@gmail.com"
PASSWORD = "123456"
PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
MARGIN_OF_ERROR = 5


def check_lat_long(lat1, long1, lat2, long2, margin):
    if (lat2 - margin <= lat1 <= lat2 + margin) and (long2 - margin <= long1 <= long2 + margin):
        return True
    return False


def make_request(url, parameters={}):
    response = get(url=url, params=parameters)
    response.raise_for_status()
    return response.json()


def make_iss_request():
    data = make_request("http://api.open-notify.org/iss-now.json")
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)


def make_sunrise_request(parameters):
    data = make_request("https://api.sunrise-sunset.org/json", parameters)
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    return (sunset, sunrise)


def main():
    if __name__ == "__main__":
        while True:
            iss_latitude, iss_longitude = make_iss_request()
            if check_lat_long(MY_LAT, MY_LONG, iss_latitude, iss_longitude, MARGIN_OF_ERROR):
                sunset, sunrise = make_sunrise_request(PARAMETERS)
                time_now = datetime.now()
                if time_now.hour >= sunset or time_now <= sunrise:
                    smtp_handler = SmtpHandler(HOST, PORT, USER, PASSWORD)
                    smtp_handler.send_message(
                        "Hey, look up to the sky, the ISS is just above", to_addrs="destination@gmail.com")
            sleep(60)


main()
