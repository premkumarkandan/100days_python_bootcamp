from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Turtle", "Guess the color of the winner?")
turtle_list = []
color_list = ["red", "blue", "green", "purple", "orange"]

step = -2

if user_bet.lower() in color_list:
    is_race_on = True

for t in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[step])
    new_turtle.goto(-200, 50 * step)
    turtle_list.append(new_turtle)
    step += 1


while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} tutle is the winner")
            else:
                print(f"You've lost! The {winning_color} tutle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()