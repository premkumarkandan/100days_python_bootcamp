from game_data import data
from art import logo 
from art import vs
import random

current_score = 0
end = False
user_choice = ""
data_list = list(range(0,50))
# x = random.randint(0,49)
x = random.choice(data_list)
data_list.remove(x)
# y = random.randint(0,49)
y = random.choice(data_list)
data_list.remove(y)
# if x == y:
#     y = random.randint(0,49)
# option_x = data[x]
# option_y = data[y]

while not end:
    if user_choice == "a":
        y = random.choice(data_list)
        # if x == y:
        #     y = random.choice(data_list)
        data_list.remove(y)
    elif user_choice == "b":
        x = y
        y = random.choice(data_list)
        # if x == y:
        #     y = random.choice(data_list)
        data_list.remove(y)
    print(logo)
    print (f"Compare A: {data[x]['name']}, {data[x]['description']}, from {data[x]['country']}")
    print(vs)
    print (f"Against B: {data[y]['name']}, {data[y]['description']}, from {data[y]['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_choice == "a":
        if data[x]['follower_count'] > data[y]['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            end = True
    elif user_choice == "b":        
        if data[y]['follower_count'] > data[x]['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}") 
            end = True 
    # print(data_list)
    if current_score > 48 :
        print("You have won the Game !!!")
        break


