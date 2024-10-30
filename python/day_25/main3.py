import pandas as pd
import turtle
from scoreboard import Scoreboard

# Set up screen and background image
screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
game_is_on = True
ans_list = []

# Turtle setup
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

scoreboard = Scoreboard()
turtle1.shape(image)    # Set turtle1 to display the image
turtle2.hideturtle()    # Hide turtle to display ttext

# Load state data
states = pd.read_csv("50_states.csv")

while game_is_on:

    # Convert the guess to title case
    answer_check = screen.textinput("Guess the State", "What's another State Name?").title()

    state_display = states[states["state"] == answer_check]
    ans_list.append(state_display["state"].values[0])

    if not state_display.empty:
        state_pos_x = state_display["x"].values[0]
        state_pos_y = state_display["y"].values[0]
        # print(state_pos_x, state_pos_y)
        # Move turtle2 to the specified coordinates
        turtle2.penup()
        turtle2.goto(state_pos_x, state_pos_y)
        # print(states)
        turtle2.write(answer_check, align="center", font=("Arial", 16, "normal"))
        states = states[~(states["state"] == answer_check)]
        scoreboard.increase_score()
    elif len(ans_list) > 49:
        print("Congratulations! You've guessed as states!")
        game_is_on = False
    else:
        game_is_on = False
        print("Enter a valid choice!!")
