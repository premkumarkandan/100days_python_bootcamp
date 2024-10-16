from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scorecard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snake Game")
snake = Snake()
food = Food()
score = Scorecard()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake movement
    snake.move()
    # snake.snake_score()
    # detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_count()
    # detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
