from smtpHandler import SmtpHandler
import pandas as pd
import datetime as dt
import random
import os

GOOGLE_SMTP = "smtp.gmail.com"
my_email = "dummyemail@gmail.com"
password = "123456"
smtp_handler = SmtpHandler(GOOGLE_SMTP, 567, my_email, password)


def check_dates(date1, date2=dt.datetime.now()):
    if date2.month == date1["month"] and date2.day == date1["day"]:
        return True
    return False


def make_letter(name, quote):
    list_of_letters = os.listdir("letter_templates/")
    random_letter = random.choice(list_of_letters)
    with open(f"letter_templates\\{random_letter}") as letter:
        letter_text = ''.join(letter.readlines())
    letter_text = letter_text.replace("[NAME]", name)
    letter_text = letter_text.replace("[QUOTE]", quote)
    return letter_text


def pick_random_quoute():
    with open("quotes.txt") as file:
        return random.choice(file.readlines())


def main():
    if __name__ == "__main__":
        birthdays = pd.read_csv("birthdays.csv")
        regs = birthdays.to_dict(orient="records")
        for birth in regs:
            if check_dates(date1=birth):
                random_quote = pick_random_quoute()
                letter = make_letter(birth["name"], random_quote)
                print(letter)
                smtp_handler.send_email(
                    birth["email"], f"Subject: Happy Birthay!\n\n{letter}")


main()
