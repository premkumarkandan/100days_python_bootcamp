import turtle
from turtle import Turtle, Screen
from color import color_list
import random

tim = Turtle()
# tim.shape("turtle")
tim.color("dark green")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.end_fill()
# for item in range (4):
#     tim.forward(100)
#     tim.right(90)

# for steps in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

turtle.colormode(255)
# direction = [0, 90, 180, 270]
# tim.circle(50)
# tim.width(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# def direction_choice():
#     tim.right(random.choice(direction))
#     tim.forward(100)


# spirograph loop
for i in range(0, 360, 10):
    tim.color(random_color())
    # direction_choice()
    tim.setheading(i)
    tim.circle(50)
    # tim.left(2)

# tim.goto(0, 50)


# for _ in range(200):
#     tim.color(random.choice(color_list))
#     direction_choice()


screen = Screen()
screen.exitonclick()
