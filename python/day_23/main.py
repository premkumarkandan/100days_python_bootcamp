import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_list = []
new_x = 240
new_y = 0

screen.listen()
screen.onkey(tim.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    print(game_is_on)
    print(car.xcor())
    if car.xcor() > -350:
        car.move_cars()
    elif car.xcor() < -350:
        game_is_on = False


screen.exitonclick()
