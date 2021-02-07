print("Welcome to Treasure Island")

print("Your mission is to find the treasure")

direction = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right': "
)

if direction == "left":
    action = input(
        "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: "
    )
    if action == "wait":
        a = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: "
        )
        if a == "red":
            print("It's a room full of fire. Game Over")
        elif a == "yellow":
            print("It's a room full of gold, good job")
        elif a == "blue":
            print("it's a room full of water, you drown. Game Over")
    elif action == "swim":
        print(
            "You try to swim but its a big body of water and you end up drowning, Game Over"
        )
elif direction == "right":
    print("There's only emptyness on the right, Game Over")