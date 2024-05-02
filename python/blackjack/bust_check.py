import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_current_score = 0
dealer_cards = []
dealer_current_score = 0
player_continue_game = True
player_choice = "n"


def player_cards_list(player_cards):
    if player_choice == "y":
        (player_cards).append(random.choice(cards))
        return player_cards    
    elif player_choice == "n":
        for card in range (0,2):
            (player_cards).append(random.choice(cards))
        return player_cards 

def player_currentscore(player_current_score):
    if player_choice == "y":
        player_current_score += player_cards[-1]
        if player_current_score > 20 and 11 in player_cards:
            player_current_score -= 10 
            return player_current_score
        return player_current_score 
    elif player_choice == "n":     
        for card in range (0,2):
            player_current_score += player_cards[card]
        if player_current_score > 20 and 11 in player_cards:
            player_current_score -= 10    
        return player_current_score    

def bust_check_cards(player_current_score,dealer_current_score):
    if player_current_score > dealer_current_score:
        print("You went over. You lose")
    elif dealer_current_score > player_current_score:
        print("You won")
    else:
        print("Draw") 

def dealer_cards_list(dealer_cards):
    if player_choice == "y":
        (dealer_cards).append(random.choice(cards))
        return dealer_cards    
    elif player_choice == "n":
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
    elif player_choice == "n":     
        for card in range (0,2):
            dealer_current_score += dealer_cards[card]
        if dealer_current_score > 20 and 11 in dealer_cards:
            dealer_current_score -= 10    
        return dealer_current_score  
player_cards = player_cards_list(player_cards)
player_current_score = player_currentscore(player_current_score)
print(f"Your cards: {player_cards}, current score: {player_current_score}")

dealer_cards = dealer_cards_list(dealer_cards)
dealer_current_score = dealer_currentscore(dealer_current_score)
print(f"Computer's first card: {dealer_cards[0]}")
print(dealer_cards,dealer_current_score)

player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
while player_choice == "y":
    if player_choice == "y":
        player_cards = player_cards_list(player_cards)
        player_current_score = player_currentscore(player_current_score)
        print(f"Your cards: {player_cards}, current score: {player_current_score}")
        bust_check_cards = bust_check_cards(player_current_score,dealer_current_score)
        dealer_cards = dealer_cards_list(dealer_cards)
        dealer_current_score = dealer_currentscore(dealer_current_score)
        print(f"Computer's first card: {dealer_cards[0]}")
        print(dealer_cards,dealer_current_score)
        if player_current_score or dealer_current_score > 20:
            # bust_check_cards = bust_check_cards(player_current_score,dealer_current_score)
            # bust_check_score = bust_check_score(player_current_score,dealer_current_score)
            print(f"Your final hand: {player_cards}, final score: {player_current_score}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_current_score}")
    elif player_choice == "n":
        break 
    player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower() 