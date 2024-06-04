import colorgram
import turtle
from turtle import Turtle, Screen
import random

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
tom = Turtle()
# tom.width(20)
tom.speed("fastest")
turtle.colormode(255)


def random_color():
    color = random.choice(color_list)
    return color


# tom.color(random_color())
#
# tom.circle(20)
# tom.fillcolor(random_color())
# tom.penup()
# tom.forward(50)
# tom.pendown()

# for row in range(1, 11):
#     for column in range(0, 11):
#         tom.color(random_color())
#         tom.pendown()
#         tom.circle(20)
#         tom.penup()
#         tom.forward(50)
#     tom.goto(0, row*50)
tom.circle(20)

for row in range(1, 11):
    for column in range(0, 11):
        tom.color(random_color())
        tom.setheading(50)
    tom.goto(0, row*50)

screen = Screen()
screen.exitonclick()

# colors = colorgram.extract('images.jpg', 25)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))
#
# # print(rgb_colors)


