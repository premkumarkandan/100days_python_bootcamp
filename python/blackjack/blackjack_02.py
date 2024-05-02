import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_current_score = 0
dealer_cards = []
dealer_current_score = 0
player_continue_game = True
player_choice = ""
game_choice = ""

def player_cards_list(player_cards):
    if player_choice == "y" and len(player_cards) > 1 :
        (player_cards).append(random.choice(cards))
        return player_cards    
    else:
        for card in range (0,2):
            (player_cards).append(random.choice(cards))
        return player_cards 

def player_currentscore(player_current_score):
    if player_choice == "y" and len(player_cards) > 1:
        player_current_score += player_cards[-1]
        if player_current_score > 20 and 11 in player_cards:
            player_current_score -= 10 
            return player_current_score
        return player_current_score 
    else:     
        for card in range (0,2):
            player_current_score += player_cards[card]
        if player_current_score > 20 and 11 in player_cards:
            player_current_score -= 10    
        return player_current_score 

def dealer_cards_list(dealer_cards):
    if player_choice == "y":
        (dealer_cards).append(random.choice(cards))
        return dealer_cards    
    else:
        for card in range (0,2):
            (dealer_cards).append(random.choice(cards))
        return dealer_cards

def dealer_currentscore(dealer_current_score):
    if player_choice == "y":
        dealer_current_score += dealer_cards[-1]
        if dealer_current_score > 20 and 11 in dealer_cards:
            dealer_current_score -= 10 
            return dealer_current_score
        return dealer_current_score 
    else:     
        for card in range (0,2):
            dealer_current_score += dealer_cards[card]
        if dealer_current_score > 20 and 11 in dealer_cards:
            dealer_current_score -= 10    
        return dealer_current_score  

def display_message():
    if player_current_score > 21:
        print("You went over. You lose")
    elif player_current_score == 21:
        print("Win with a Blackjack 😎")
    elif dealer_current_score == 21:
        print("Opponent won with a Blackjack ")        
    elif dealer_current_score > 21 or player_current_score == 21:
        print("You won")
    else:
        print("Draw") 
    pass

def bust_check(player_current_score):
    if player_current_score > 21:
        print("You went over. You lose")
        return "n"
    elif dealer_current_score > 21 or player_current_score == 21:
        print("You won")
        return "n"
    else:
        pass       

def blackjack_check(player_cards,dealer_cards):
    if 10 and 11 in  player_cards :
        if len(player_cards) < 3:
            print("Win with a Blackjack 😎")
            return True
    elif 10 and 11 in dealer_cards :
        if len(dealer_cards) < 3:
            print("Opponent won with a Blackjack")
            return True
    else:
        pass  

def choice(game_choice,player_choice):
    game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    return          

game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# game_choice = choice(game_choice,player_choice)
while game_choice == "y":
    player_cards = player_cards_list(player_cards)
    player_current_score = player_currentscore(player_current_score)
    dealer_cards = dealer_cards_list(dealer_cards)
    dealer_current_score =  dealer_currentscore(dealer_current_score)
    print(f"Your cards: {player_cards}, current score: {player_current_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    check = blackjack_check(player_cards,dealer_cards)
    if check is True:
        game_choice == "n"
        break
    else:
        pass
    if player_choice == "y":
        player_cards = player_cards_list(player_cards)
        player_current_score = player_currentscore(player_current_score)
        print(f"Your cards: {player_cards}, current score: {player_current_score}")
        print(f"Computer's first card: {dealer_cards[0]}")
        bust_check(player_current_score)
    elif player_choice == "n":
        break
    player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower() 
    # game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() 
