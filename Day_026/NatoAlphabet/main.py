from data import DATA


def make_alphabet_from_word(word):
    return [DATA[w.upper()] for w in list(word)]


def make_alphabet_string(word):
    return "\n".join([f"{w.upper()} as in {DATA[w.upper()]}" for w in list(word)])


def main():
    if __name__ == "__main__":
        print("Welcome to the nato alphabet converter")
        name = input("Enter a phrase: ")

        aplhabet = make_alphabet_from_word(name)
        aplhabet_str = make_alphabet_string(name)

        print(aplhabet, end="\n\n")
        print(aplhabet_str, end="\n\n")


main()