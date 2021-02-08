import random

print("Welcome to the password generator")

n_of_chars = int(input("How many letters long: "))
n_of_symbols = int(input("How many symbols do you want: "))
n_of_numbers = int(input("How many numbers do you want: "))


password = ""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["$", "%", "#", "!", "&", "*", "_", "~"]
chars = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


for n in range(0, n_of_numbers):
    password += str(random.choice(numbers))

for n in range(0, n_of_symbols):
    password += random.choice(symbols)

for n in range(len(password), n_of_chars):
    password += random.choice(chars)

randomized_password = list(password)
random.shuffle(randomized_password)
randomized_password = "".join(randomized_password)

print(f"Your password is: {randomized_password}")
