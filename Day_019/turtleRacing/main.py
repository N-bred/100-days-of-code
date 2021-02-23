from turtle import Turtle, Screen
import random

screen = Screen()

width, height = 500, 400

screen.setup(width, height)
color_to_win = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def draw_turtles():
    for i, color in list(enumerate(colors)):
        tim = Turtle(shape="turtle")
        tim.color(color)
        tim.penup()
        tim.goto(x=-230, y=-100 + i * 40)
        turtles.append(tim)


draw_turtles()


def declare_winner(turtle):
    if turtle.color()[0] == color_to_win:
        print("Congratulations, you win")
    else:
        print(f"You lose lol, the winner was: {turtle.color()[0]}")


is_running = True
while is_running:
    for turtle in turtles:
        turtle.forward(random.randint(0, 15))

        if turtle.pos()[0] >= width / 2:
            declare_winner(turtle)
            is_running = False
            break


screen.exitonclick()