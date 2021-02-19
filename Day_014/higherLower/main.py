import random
from data import data


def pick_random_item(arr):
    random_pick = random.choice(arr)
    arr.remove(random_pick)
    return random_pick


def format_string(item):
    return f"{item['name']} is a {item['description']} from {item['country']}"


def main():
    if __name__ == "__main__":
        print("Welcome to the higher or lower game")
        score = 0
        left_side = pick_random_item(data)
        right_side = pick_random_item(data)

        while True:
            print("Who has more followers? Type A or B to choose your answer.")
            print(f"Option A is: {format_string(left_side)}")
            print(f"Option B is: {format_string(right_side)}")

            answer = input("Option: ")

            if answer.lower() == "a":
                if left_side["follower_count"] >= right_side["follower_count"]:
                    score += 1
                    right_side = pick_random_item(data)
                else:
                    break
            elif answer.lower() == "b":
                if right_side["follower_count"] >= left_side["follower_count"]:
                    score += 1
                    left_side = right_side
                    right_side = pick_random_item(data)
                else:
                    break
            else:
                return print("Wrong option")

        return print(f"Your score was: {score}")


main()