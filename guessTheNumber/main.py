import random


def main():
    if __name__ == "__main__":
        print("Welcome to the guessing number game.")

        difficulty = input("Select a difficulty: Easy or Hard:  ")
        initial_number = int(input("Type the initial range as a number: "))
        final_number = int(input("Type the final range as a number: "))

        lifes = 0

        if difficulty.lower() == "easy":
            lifes = 10
        elif difficulty.lower() == "hard":
            lifes = 5
        else:
            return print("Wrong choice of difficulty")

        if final_number <= initial_number:
            return print("Final range cannot be lower or the same as intial range")

        magic_number = random.randint(initial_number, final_number)

        while True:
            input_number = int(input("Guess the magic number "))
            if input_number == magic_number:
                return print(f"You guessed it! Magic number was: {magic_number}")

            if input_number < magic_number:
                print("Number is lower than the magic number")
            else:
                print("Number is higher than the magic number")

            lifes -= 1

            print(f"Lifes: {lifes}")

            if lifes <= 0:
                break

        return print("You lose!")


main()