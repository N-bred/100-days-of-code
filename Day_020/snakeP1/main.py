from turtle import Screen, Turtle
from snake import Snake
import time

WIDTH, HEIGHT = 600, 600


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)


snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()


screen.exitonclick()