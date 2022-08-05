import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    #detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False


    #detect collision with final wall
    if player.finish_line():
        player.go_back()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()