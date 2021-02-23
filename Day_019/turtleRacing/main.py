from turtle import Turtle, Screen
import random

WIDTH, HEIGHT = 500, 400
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def get_colors(colors):
    return "\n- ".join(colors)


def draw_turtles(colors):
    turtles = []
    for i, color in list(enumerate(colors)):
        tim = Turtle(shape="turtle")
        tim.color(color)
        tim.penup()
        tim.goto(x=-230, y=-100 + i * 40)
        turtles.append(tim)
    return turtles


def declare_winner(turtle, win_color):
    if turtle.color()[0] == win_color:
        print("Congratulations, you win")
    else:
        print(f"You lose lol, the winner was: {turtle.color()[0]}")


def main():
    if __name__ == "__main__":
        screen = Screen()
        screen.setup(WIDTH, HEIGHT)
        chose_color = screen.textinput(
            title="Make your bet",
            prompt=f"Which turtle will win the race? Enter a color ({get_colors(COLORS)}): ",
        )
        turtles = draw_turtles(COLORS)
        is_running = True
        while is_running:
            for turtle in turtles:
                turtle.forward(random.randint(0, 15))

                if turtle.pos()[0] >= WIDTH / 2:
                    declare_winner(turtle, chose_color)
                    is_running = False
                    break
        screen.exitonclick()


main()