from color import color_list
import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
tom.speed("fastest")
turtle.colormode(255)
x0 = -250
y0 = -250
step = 0
tom.penup()
tom.goto(x0, y0)
tom.dot(20, random.choice(color_list))


def random_color():
    color = random.choice(color_list)
    return color


for _ in range(10):
    tom.setpos(x0, y0+step)
    for c_ in range(10):
        tom.dot(20, random.choice(color_list))
        tom.forward(50)
    step += 50
    # tom.goto(x0, y0+50)

tom.ht()
screen = Screen()
screen.exitonclick()



