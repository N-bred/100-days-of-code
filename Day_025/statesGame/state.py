from turtle import Turtle


class State(Turtle):
    def __init__(self, title, pos):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.write(title)
