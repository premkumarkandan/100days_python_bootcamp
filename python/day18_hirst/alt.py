from color import color_list
from turtle import Turtle, Screen
from random import choice

# Initialization

leo = Turtle()
# leo.shape("turtle")
my_screen = Screen()

# Setting parameters

my_screen.colormode(255)
leo.penup()
x0 = -250
y0 = -250
leo.setpos(x0, y0)

step = 0

# Start animation

for _ in range(10):
    leo.setpos(x0, y0 + step)
    for _ in range(10):
        leo.dot(20, choice(color_list))
        leo.forward(50)
    step += 50

leo.ht()

my_screen.exitonclick()