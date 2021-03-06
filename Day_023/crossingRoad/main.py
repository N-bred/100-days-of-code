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
scoreBoard = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreBoard.increase_level()
        car_manager.reset()

screen.exitonclick()