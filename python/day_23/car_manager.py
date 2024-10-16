# Import necessary modules from turtle for visualizations and random for random generation
from turtle import Turtle
import random

# Constant values for car movement and starting position
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # The starting speed of the car
MOVE_INCREMENT = 10  # Speed increment as game progresses

# CarManager class handles the creation and movement of cars


class CarManager:

    def __init__(self):
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Set initial speed of cars

    # Function to randomly create a new car
    def create_car(self):
        # Randomly decide if a car should be created (1 in 6 chance)
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Each car is a square turtle object
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch shape to resemble a car
            new_car.penup()  # Ensure the car doesn't leave any trail
            new_car.color(random.choice(COLORS))  # Randomly assign one of the colors
            # Set the initial position for the car (random y-coordinate across the screen width)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # Starts from right edge of screen
            self.all_cars.append(new_car)  # Add the car to the list of all cars

    # Function to move all cars leftward (i.e., simulate movement along x-axis)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car at the current speed

    # Function to increase the speed of cars when called (e.g., level up)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase speed by increment
