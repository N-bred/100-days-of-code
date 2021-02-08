import random
from string import ascii_lowercase, ascii_uppercase


def main():
    if __name__ == "__main__":
        print("Welcome to the password generator")
        n_of_chars = int(input("How many letters long: "))
        n_of_symbols = int(input("How many symbols do you want: "))
        n_of_numbers = int(input("How many numbers do you want: "))
        allow_uppercase = int(
            input("Allow uppercase letters? press 1 to allow or 0 to avoid: ")
        )

        numbers = [n for n in range(0, 9)]
        symbols = ["$", "%", "#", "!", "&", "*", "_", "~"]
        password = ""

        for n in range(0, n_of_numbers):
            password += str(random.choice(numbers))

        for n in range(0, n_of_symbols):
            password += random.choice(symbols)

        for n in range(len(password), n_of_chars):
            if allow_uppercase == 1:
                if random.random() > 0.5:
                    password += random.choice(ascii_uppercase)
                else:
                    password += random.choice(ascii_lowercase)
            else:
                password += random.choice(ascii_lowercase)

        randomized_password = list(password)
        random.shuffle(randomized_password)
        randomized_password = "".join(randomized_password)
        return print(f"Your password is: {randomized_password}")


main()