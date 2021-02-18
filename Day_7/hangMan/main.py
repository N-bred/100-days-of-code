import random
import os

scenes = [
    "",
    """
       o""",
    """
       o
       |""",
    """
       o
      /|""",
    """
       o
      /|\\""",
    """
       o
      /|\\
      /""",
    """
       o
      /|\\
      / \\""",
]

words = [
    "car",
    "gatekeeper",
    "inquisitor",
    "dark",
    "souls",
    "animals",
    "mechanical",
    "shadows",
    "twice",
]


def find_indexes(string, char):
    if char not in string:
        return False
    return [i for i, ch in enumerate(string) if ch == char]


def replace_space(space_list, indexes, char):
    for i in indexes:
        space_list[i] = char
    return "".join(space_list)


def main():
    if __name__ == "__main__":
        deaths = 0
        word = random.choice(words)
        spaces_list = ["_" for w in list(word)]
        spaces_str = "".join(spaces_list)

        print("Welcome to the Hangman")

        while deaths < len(scenes) - 1:
            if spaces_str == word:
                return print(f"Correct word: {word}\n\nYou win!\nGame Over")

            print(spaces_str, end="\n\n")
            print(scenes[deaths])

            ch = input("Enter a letter: ")

            if ch in spaces_str:
                print("Letter already used")
                continue

            indexes = find_indexes(word, ch)
            if indexes is not False:
                spaces_str = replace_space(spaces_list, indexes, ch)
            else:
                deaths += 1
            os.system("cls")

        return print(f"Correct word: {word}\n\nYou lose :(\nGame Over")


main()
