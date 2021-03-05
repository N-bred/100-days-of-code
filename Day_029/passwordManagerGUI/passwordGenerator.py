import random
from string import ascii_lowercase, ascii_uppercase


def create_random_password(n_of_digits=10, allow_uppercase=True, allow_symbols=True, allow_numbers=True):
    password_array = []
    choices = {"chars": {"lower": ascii_lowercase}}

    if allow_uppercase:
        choices["chars"]["upper"] = ascii_uppercase
    if allow_symbols:
        choices["symbols"] = ["$", "%", "#", "!", "&", "*", "_", "~"]
    if allow_numbers:
        choices["numbers"] = [str(n) for n in range(0, 9)]

    while len(password_array) < n_of_digits:
        random_key = random.choice(list(choices.keys()))
        if random_key == "chars":
            random_chars_key = random.choice(list(choices[random_key].keys()))
            password_array.append(random.choice(
                choices[random_key][random_chars_key]))
        else:
            password_array.append(random.choice(choices[random_key]))

    random.shuffle(password_array)
    return ''.join(password_array)
