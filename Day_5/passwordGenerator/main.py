import random
from string import ascii_lowercase, ascii_uppercase


def create_random_password(n_of_chars, n_of_symbols, n_of_numbers, allow_uppercase):
    numbers = [n for n in range(0, 9)]
    symbols = ["$", "%", "#", "!", "&", "*", "_", "~"]
    password = []

    for n in range(0, n_of_numbers):
        password.append(str(random.choice(numbers)))

    for n in range(0, n_of_symbols):
        password.append(random.choice(symbols))

    for n in range(len(password), n_of_chars):
        if allow_uppercase == 1:
            selected = ascii_lowercase
            if random.random() > 0.5:
                selected = ascii_uppercase
            password.append(random.choice(selected))
        else:
            password.append(random.choice(ascii_lowercase))

    random.shuffle(password)
    return "".join(password)


def main():
    if __name__ == "__main__":
        print("Welcome to the password generator")
        n_of_chars = int(input("How many letters long: "))
        n_of_symbols = int(input("How many symbols do you want: "))
        n_of_numbers = int(input("How many numbers do you want: "))
        allow_uppercase = int(
            input("Allow uppercase letters? press 1 to allow or 0 to avoid: ")
        )

        random_password = create_random_password(
            n_of_chars, n_of_symbols, n_of_numbers, allow_uppercase
        )
        return print(f"Your password is: {random_password}")


main()