import random
from art import logo

# creating variable to represent the Jack, Queen, King and Ace
J = 10
K = 10
Q = 10
A = 11

# Creating a dec of card
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q]

# function to calculate the score of players
def score(chosen_card_list):
    total_score =0
    for i in chosen_card_list:
        total_score += i
    return total_score

# function that will add new cards to the dealer's pack
def add_new_cards_dealer(chosen_card_list, total_score):
    while total_score<21:
        chosen_card_list.append(random.choice(cards))
        total_score = score(chosen_card_list)
    # implementing a Black_jack rule regarding Ace
    if A in chosen_card_list and total_score > 21:
        total_score -= 10
    print(f"Dealer's Updated Cards are {chosen_card_list}")
    print(f"Dealer's New Total_Score ={total_score}")
    return total_score

# creating Black_jack function which will customise and process the whole game
def Black_jack():
    continue_or_not = 'yes'

    # Player can play many times
    while continue_or_not == 'yes':
        print(logo)
        # Initial serve of cards
        Players_hand = [random.choice(cards), random.choice(cards)]
        Dealers_hand = [random.choice(cards)]

        print(f"Player's cards are = {Players_hand}")
        print(f"Dealer's card are = {Dealers_hand}")

        if score(Players_hand) == 21:
            print("you win")
        # printing the initial status
        print(f"Your score is = {score(Players_hand)}\n The Dealer's score is = {score(Dealers_hand)}")

        # asking stance from the player
        Hit_Stand = input("Enter H/h for HIT and S/s for Stand\n").lower()

        # if user chooses to hit
        while Hit_Stand == 'h':
            Players_hand.append(random.choice(cards))
            print(f"Player's card are = {Players_hand}")
            players_score = score(Players_hand)
            if A in Players_hand and players_score>21:
                players_score -= 10

            print(f"Your score is = {players_score}\n The Dealer's score is = {score(Dealers_hand)}\n")

            if score(Players_hand) > 21:
                print("you lose")
                break
            if score(Players_hand) == 21:
                print("you win")
                break
            Hit_Stand = input("Enter H/h for HIT and S/s for Stand\n").lower()
        # if a user chooses to stand
        if Hit_Stand == "s":
            Dealers_hand.append(random.choice(cards))
            dealers_score = score(Dealers_hand)
            # evaluating the score according to the wining criteria
            if A in Dealers_hand and dealers_score > 21:
                dealers_score -= 10
            print(f"Dealer's card are = {Dealers_hand}")
            print(f"Your score is = {score(Players_hand)}\nThe Dealer's score is = {dealers_score}")
            if score(Dealers_hand) >= 17 and 21 >= score(Dealers_hand) > score(Players_hand):
                print("You Lose")
            elif score(Dealers_hand) < 17:
                new_total_score = add_new_cards_dealer(Dealers_hand, score(Dealers_hand))
                if 21 >= new_total_score > score(Players_hand):
                    print("You lose")
                elif new_total_score == score(Players_hand):
                    print("Draw")
                else:
                    print("You win")
            else:
                print("Draw")

        # Asking the user to play another game or quit
        continue_or_not = input("Enter 'yes' to CONTINUE and 'no' to EXIT\n")
Black_jack()



