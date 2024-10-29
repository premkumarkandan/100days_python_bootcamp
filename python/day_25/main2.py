import turtle
import pandas as pd
from scoreboard import Scoreboard

# Set up screen and background image
screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
game_is_on = True
# Turtle setup
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
scoreboard = Scoreboard()
turtle1.shape(image)    # Set turtle1 to display the image
turtle2.hideturtle()

# User input to guess a state
answer_state = screen.textinput("Guess the State", "What's another State Name?")
answer_check = answer_state.title()

# Load state data
states_data = pd.read_csv('50_states.csv')
state_display = states_data[states_data["state"] == answer_check]
if answer_check in states_data:
    print("yes")

while game_is_on:
    if states_data.empty:
        game_is_on = False
    # Get x, y coordinates from the DataFrame for the guessed state
    if not state_display.empty:
        state_pos_x = state_display["x"].values[0]
        state_pos_y = state_display["y"].values[0]

        # Move turtle2 to the specified coordinates
        turtle2.penup()
        turtle2.goto(state_pos_x, state_pos_y)
        turtle2.write(answer_check, align="center", font=("Arial", 16, "normal"))
        states_data.pop(state_display)
        scoreboard.increase_score()
    else:
        print("State not found in the dataset.")

# Keep the screen open
screen.mainloop()
