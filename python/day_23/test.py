import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Turtle()
tim.shape("square")
tim.penup()
tim.speed("slow")
tim.color("red")
tim.shapesize(stretch_wid=1, stretch_len=1.5)
tim.goto(350, 0)
game_is_on = True
new_x = 350
new_y = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if tim.xcor() > -350:
        tim.goto(new_x, new_y)
        new_x += -10
    elif tim.xcor() < -350:
        game_is_on = False

screen.exitonclick()
