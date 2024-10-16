from turtle import Turtle
from color import color_list
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        # self.speed("fastest")
        self.ball_motion_speed = 0.1
        self.step_x = 10
        self.step_y = 10
        self.ball_out_1 = False
        self.ball_out_2 = False

    def ball_motion(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)
        self.clear()

    def ball_bounce_y(self):
        self.step_y *= -1
        self.ball_motion_speed *= 0.9

    def ball_bounce_x(self):
        self.step_x *= -1
        self.ball_motion_speed *= 0.9

    def ball_out_of_bounds(self):
        self.home()
        self.ball_bounce_x()
        self.ball_motion_speed = 0.1
        self.color("white")

    def ball_color_change(self):
        self.color(random.choice(color_list))







