from turtle import Screen, Turtle
import time

WIDTH, HEIGHT = 600, 600


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]


segments = []

for pos in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)


screen.exitonclick()