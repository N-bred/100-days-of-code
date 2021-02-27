from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

WIDTH, HEIGHT = 600, 600


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)


player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()