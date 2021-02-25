from turtle import Screen
from snake import Snake
from food import Food
import time

WIDTH, HEIGHT = 600, 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)


snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()