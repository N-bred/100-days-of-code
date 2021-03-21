from dotenv import load_dotenv
import os
import requests
load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"

PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}


def make_request(url=STOCK_API_ENDPOINT, params=PARAMS):
    req = requests.get(url, params)
    req.raise_for_status()
    return req.json()


def make_message(percentage, direction="up"):
    return f"{STOCK}: {direction}{percentage}%"


def format_data(data):
    data[1]["date"] = data[0]
    return data[1]


def eval_data(json_data):
    stock_data = [format_data(data)
                  for data in json_data["Time Series (Daily)"].items()][:2]
    close1, close2 = float(stock_data[0]["4. close"]), float(
        stock_data[1]["4. close"])
    percentage = (close1 - close2) / close1

    if percentage >= 0.05:
        return (percentage, 'up')
    elif percentage <= -0.05:
        return (percentage, 'down')
    return False


def main():
    data = make_request()
    value = eval_data(data)
    if type(value) is not bool:
        message = make_message(value[0], value[1])
        return print(message)
    return print("No substantial changes")


if __name__ == "__main__":
    main()

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
