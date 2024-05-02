import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_current_score = 0
dealer_cards = []
dealer_current_score = 0
player_continue_game = True
player_choice = "n"

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

dealer_cards = dealer_cards_list(dealer_cards)
dealer_current_score = dealer_currentscore(dealer_current_score)
print(f"Computer's first card: {dealer_cards[0]}")
print(dealer_cards,dealer_current_score)

player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
while player_choice == "y":
    if player_choice == "y":
        # player_cards = player_cards_list(player_cards)
        # player_current_score = player_currentscore(player_current_score)
        # print(f"Your cards: {player_cards}, current score: {player_current_score}")
        dealer_cards = dealer_cards_list(dealer_cards)
        dealer_current_score = dealer_currentscore(dealer_current_score)
        print(f"Computer's first card: {dealer_cards[0]}")
        print(dealer_cards,dealer_current_score)
    elif player_choice == "n":
        break 
    player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower() 