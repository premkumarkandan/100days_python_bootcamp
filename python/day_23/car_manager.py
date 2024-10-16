import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_x = []
        self.car_y = []
        self.pos_x = 0
        self.pos_y = 0
        self.rand_xy()
        self.generate_cars()

    def rand_xy(self):
        for _ in range(-300, 300, 10):
            self.car_x.append(_)
            self.car_y.append(_)

    def generate_cars(self):
        self.pos_x = random.choice(self.car_x)
        self.pos_y = random.choice(self.car_y)
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.goto(self.pos_x, self.pos_y)
        # self.car_list.append(self)

    def move_cars(self):
        self.goto(self.pos_x, self.pos_y)
        self.pos_x -= 5

