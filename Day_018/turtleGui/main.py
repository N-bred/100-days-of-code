import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

colors = [
    (245, 243, 238),
    (247, 242, 244),
    (240, 245, 241),
    (202, 164, 109),
    (238, 240, 245),
    (150, 75, 49),
    (223, 201, 135),
]


def random_color(colors):
    return random.choice(colors)


n_of_dots = 100

turtle.setheading(100)
turtle.forward(100)
turtle.setheading(0)

for dot_count in range(n_of_dots):
    turtle.dot(20, random_color(colors))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()