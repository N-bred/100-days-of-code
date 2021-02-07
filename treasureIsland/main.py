questions = {
    "question": "You're at a cross road. Where do you want to go? Type 'left' or 'right': ",
    "options": {
        "left": {
            "question": "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ",
            "options": {
                "wait": {
                    "question": "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: ",
                    "options": {
                        "red": {"gameover": "It's a room full of fire. Game Over"},
                        "yellow": {"gameover": "It's a room full of gold, good job"},
                        "blue": {
                            "gameover": "it's a room full of water, you drown. Game Over"
                        },
                    },
                },
                "swim": {
                    "gameover": "You try to swim but its a big body of water and you end up drowning, Game Over"
                },
            },
        },
        "right": {"gameover": "There's only emptyness on the right, Game Over"},
    },
}


def ask_question(question):
    if "gameover" in question:
        return print(question["gameover"])

    answer = input(question["question"])

    if answer == "exit":
        return print("Goodbye!")
    if answer in question["options"]:
        return ask_question(question["options"][answer])
    else:
        print("bad answer")
        return ask_question(question)


def main():
    if __name__ == "__main__":
        print("Welcome to Treasure Island")
        print("Your mission is to find the treasure")
        ask_question(questions)


main()