import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carManager = CarManager()


scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key='Up', fun=player.up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move()

    if player.ycor() > 280:
        player.reset_pos()
        scoreboard.add_level()
        carManager.add_speed()

    for car in carManager.allcars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()