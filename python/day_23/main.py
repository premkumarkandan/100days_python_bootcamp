from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Set up the screen where the game happens
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic updates for smoother animations

# Create instances of Player, CarManager, and Scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up the key listener for player movement (arrow up to move up)
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True  # Game loop control variable
while game_is_on:
    time.sleep(0.1)  # Control the game speed
    screen.update()  # Update the screen after every loop

    car_manager.create_car()  # Generate new cars periodically
    car_manager.move_cars()  # Move all cars on the screen

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If car gets too close to player, game over
            game_is_on = False
            scoreboard.game_over()  # Display game over message

    # Detect if player has reached the top
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player to starting position
        car_manager.level_up()  # Increase car speed
        scoreboard.increase_level()  # Increase the score

screen.exitonclick()  # Exit the game when screen is clicked
