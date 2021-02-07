from random import randint

options = {
    0: {"name": "Rock", "relation": 2},
    1: {"name": "Paper", "relation": 0},
    2: {"name": "Scissors", "relation": 1},
}


def main():
    if __name__ == "__main__":
        print("Welcome to the Rock - Paper - Scissors game")
        n = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))

        if n < 0 or n > 2:
            print("Bad answer")
            return main()

        rn = randint(0, 2)

        print(f"You choose {options[n]['name']}")
        print(f"The computer choose {options[rn]['name']}")

        if rn == n:
            print("Draw")
        elif options[n]["relation"] == rn:
            print("You win")
        elif options[rn]["relation"] == n:
            print("You lose")


main()