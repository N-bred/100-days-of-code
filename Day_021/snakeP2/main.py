from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH, HEIGHT, TRESHOLD = 600, 600, 20
w_distance = WIDTH / 2 - TRESHOLD
h_distance = HEIGHT / 2 - TRESHOLD

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        snake.extend()
        scoreboard.increase_score()
        scoreboard.write_score()

    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()

    if (
        x_cor > w_distance
        or x_cor < -w_distance
        or y_cor > h_distance
        or y_cor < -h_distance
    ):
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()