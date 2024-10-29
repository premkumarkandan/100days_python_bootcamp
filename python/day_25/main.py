import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.shape(image)
turtle2.shape("turtle")

answer_state = screen.textinput("Guess the State", "What's another State Name?")
answer_check = answer_state.title()

states_data = pd.read_csv('50_states.csv')
state_display = states_data[states_data["state"]== answer_check]
print(state_display)

state_pos_x = state_display["x"]
state_pos_y = state_display["y"]
turtle2.penup()
turtle2.goto(state_pos_x, state_pos_y)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()