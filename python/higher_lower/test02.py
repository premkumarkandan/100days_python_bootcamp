from game_data import data
from art import logo 
from art import vs
import random

#initialize the variables
current_score = 0
end = False
user_choice = ""

#creating a data list for accessing the list of dictionaries
data_list = list(range(0,len(data)))

#generating two random variables for the options A and B
x = random.choice(data_list)
data_list.remove(x)
y = random.choice(data_list)
data_list.remove(y)

#function to generate y depending on the user choice
def choice():
    """assign values to the choices based on user input"""
    y = random.choice(data_list)
    data_list.remove(y)
    return y

#validating the choice from the user
def choice_validation(current_score):
    """compare the follower count from the user input and display the result"""
    global end
#depending the user choice check the result, do necessary operations    
    if user_choice == "a":
        if data[x]['follower_count'] > data[y]['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
            return current_score
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            end = True
    elif user_choice == "b":        
        if data[y]['follower_count'] > data[x]['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
            return current_score
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}") 
            end = True 

#printing the choices
def choice_print():
    """print the compare messages depending on the current values"""
    print(logo)
    print (f"Compare A: {data[x]['name']}, {data[x]['description']}, from {data[x]['country']}")
    print(vs)
    print (f"Against B: {data[y]['name']}, {data[y]['description']}, from {data[y]['country']}")

#main execution block
def game():
    """main game execution function"""
#declare global variables inside function to access them    
    global current_score ,x,y, user_choice
#while loop to keep executing until user input becomes wrong    
    while not end:
#if the score is longer than the data_list stop the execution
        if current_score > (len(data)-2) :
            print("You have won the Game !!!")
            break
        if user_choice == "a":
#calling the choice function to assign values from dictionary
            y = choice()
        elif user_choice == "b":
#for choice "b" have to move y to x as per requirement            
            x = y
#calling the choice function to assign values from dictionary            
            y = choice()
#cheat for manual execution
        print(x,y)
#calling the printing function        
        choice_print()
#get input from user for answer        
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

#if-elseif for choice validation
        if user_choice == "a":
            current_score = choice_validation(current_score)
        elif user_choice == "b":
            current_score = choice_validation(current_score)         

#main block execution
game()

