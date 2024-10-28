import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput("Guess the State", "What's another State Name?")
answer_check = answer_state.lower()
states_data = pd.read_csv('50_states.csv')
print(states_data)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()