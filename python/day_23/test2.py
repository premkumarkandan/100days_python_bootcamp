import time, random
from turtle import Screen, Turtle

rand_x = []
rand_y = []
for _ in range(-300, 300, 10):
    rand_x.append(_)
    rand_y.append(_)
print(rand_y)
print(rand_x)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
game_is_on = True

tim = Turtle()
tim_x = random.choice(rand_x)
tim_y = random.choice(rand_y)
tim.shape("square")
tim.penup()
tim.color(random.choice(COLORS))
tim.shapesize(stretch_wid=1, stretch_len=1.5)
tim.goto(tim_x, tim_y)

tom = Turtle()
tom_x = random.choice(rand_x)
tom_y = random.choice(rand_y)
tom.shape("square")
tom.penup()
tom.color(random.choice(COLORS))
tom.shapesize(stretch_wid=1, stretch_len=1.5)
tom.goto(tom_x, tom_y)


sam = Turtle()
sam_x = random.choice(rand_x)
sam_y = random.choice(rand_y)
sam.shape("square")
sam.penup()
sam.color(random.choice(COLORS))
sam.shapesize(stretch_wid=1, stretch_len=1.5)
sam.goto(sam_x, sam_y)

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if tim.xcor() > -350:
        tim.goto(tim_x, tim_y)
        tim_x -= 10
    elif tim.xcor() < -350:
        game_is_on = False
    if tom.xcor() > -350:
        tom.goto(tom_x, tom_y)
        tom_x -= 10
    elif tom.xcor() < -350:
        game_is_on = False
    if sam.xcor() > -350:
        sam.goto(sam_x, -150)
        sam_x -= 10
    elif sam.xcor() < -350:
        game_is_on = False

screen.exitonclick()
