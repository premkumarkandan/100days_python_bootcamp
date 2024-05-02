############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
player_current_score = 0
dealer_cards = []
dealer_current_score = 0
player_continue_game = True
player_choice = "n"

while player_continue_game is True:
    def player_cards_list(player_cards):
        if player_additional_card_choice == "y":
            (player_cards).append(random.choice(cards))
            return player_cards    
        elif player_additional_card_choice == "n":
            for card in range (0,2):
                (player_cards).append(random.choice(cards))
            return player_cards 

    def player_currentscore(player_current_score):
        if player_additional_card_choice == "y":
            player_current_score += player_cards[-1]
            if player_current_score > 20 and 11 in player_cards:
                player_current_score -= 10    
                print(player_current_score)
                return player_current_score 
        # player_current_score = 0
        elif player_additional_card_choice == "n":     
            for card in range (0,2):
                player_current_score += player_cards[card]
            if player_current_score > 20 and 11 in player_cards:
                player_current_score -= 10    
            return player_current_score    

    def dealer_cards_list(dealer_cards):
        dealer_cards = []
        for card in range (0,2):
            (dealer_cards).append(random.choice(cards))
        return dealer_cards

    def dealer_currentscore(dealer_current_score):
        dealer_current_score = 0
        for card in range (0,2):
            dealer_current_score += dealer_cards[card]    
        return dealer_current_score    

    def final_hand_check(player_current_score,dealer_current_score):
        pass

    def hand_check(player_current_score):
        pass   
        
    def player_additional_card_choice(player_cards):
        if player_additional_card_choice == "y":
            player_cards_list(player_cards)
            return player_cards

    def player_additional_card_score(player_current_score):
        if player_additional_card_choice == "y":
            player_currentscore(player_current_score)

    def player_continue_game():
        if player_continue_game == "y":
            player_continue_game = True
        elif player_continue_game == "n":
            player_continue_game = False

    def blackjack():
        pass
    
    player_cards = player_cards_list(player_cards)
    player_current_score = player_currentscore(player_current_score)
    print(f"Your cards: {player_cards}, current score: {player_current_score}")

    dealer_cards = dealer_cards_list(dealer_cards)
    dealer_current_score = dealer_currentscore(dealer_current_score)
    print(f"Computer's first card: {dealer_cards[0]}")
    player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
    while player_choice == "y":
    #     player_cards = player_cards_list(player_cards)
    #     player_current_score = player_currentscore(player_current_score)
    #     print(f"Your cards: {player_cards}, current score: {player_current_score}")

    #     dealer_cards = dealer_cards_list(dealer_cards)
    #     dealer_current_score = dealer_currentscore(dealer_current_score)
    #     print(f"Computer's first card: {dealer_cards[0]}")
        
        player_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if player_choice == "y":
            # player_additional_card_choice(player_cards)
            player_cards_list(player_cards)
            # player_additional_card_score(player_current_score)
            player_currentscore(player_current_score)
            print(f"Your cards: {player_cards}, current score: {player_current_score}")
        elif player_choice == "n":
            print(player_continue_game)
            player_continue_game()


