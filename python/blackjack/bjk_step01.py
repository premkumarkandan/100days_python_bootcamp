import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_current_score = 0
dealer_cards = []
dealer_current_score = 0
player_continue_game = True
player_choice = ""
game_choice = ""
player_win = False
dealer_win = False
check = False

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

def initial_check(player_cards,dealer_cards):
    if 10 and 11 in player_cards:
        player_win = True
        return player_win
    elif 10 and 11 in dealer_cards:
        dealer_win = True  
        return dealer_win  
    pass

def score_check():
    pass

game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while game_choice == "y":
    player_cards = player_cards_list(player_cards)
    player_current_score = player_currentscore(player_current_score)
    if player_choice == "":
        dealer_cards = dealer_cards_list(dealer_cards)
        dealer_current_score =  dealer_currentscore(dealer_current_score)
    if player_current_score == 21:
        check = initial_check(player_cards)
    if dealer_current_score == 21:
        check = initial_check(dealer_cards)        
    while check:
        if player_win == True:
            print("User has blackjack")
            game_choice = "n"
        elif dealer_win == True:
            print("Computer has blackjack") 
            game_choice = "n"           
        break        
    if player_current_score or dealer_current_score > 21:
        check = score_check()
    print(f"Your cards: {player_cards}, current score: {player_current_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    print(player_current_score)
    print(dealer_current_score)
    player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower() 
