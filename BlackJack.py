# importing relevant libraries

import os  # For operative system commands
import random # For random number generator


# user chooses number of decks of cards to use
decks = input("Enter number of decks to use: ")

# possible amount of decks
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# initialize scores
bank = 200
winnings = 0
wins = 0
losses = 0


""" function for giving a card in the deck """
def deal(deck):

    # Hand array starts out empty
    hand = []
    

    for i in range(2):

        # shuffles the deck
        random.shuffle(deck)
        try:

            # chooses a random card in the deck
            card = deck.pop()

        # checks if there are no more cards in the deck
        except IndexError as e:
            print("No more cards in the deck!")
            exit()
            

        # if the card numbers are above 10, they get their representive
        # face card name
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"

        # put chosen card in the hand array
        hand.append(card)
    
    # hand array is returned
    return hand

""" If the player wants to play again, they can type Y or N (yes or no), 
this function handles if the user wants to play again or quit """

def play_again():

    # user can input their choice
    again = input("Do you want to play again? (Y/N) : ").lower()
    
    # if user types y, the dealer and player hand empties, and we get a new deck
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    
    # if user input is n, the program exits
    else:
        print("Bye!")
        exit()


""" Function that adds and calculates the total hand value """
def total(hand):

    # we keep track of the total hand value
    total = 0

    for card in hand:

        # any face card will equal to 10 in total
        if card == "J" or card == "Q" or card == "K":
        
            total+= 10
        # Here we control if the Ace is 1 or 11 so we don't bust
        elif card == "A":
        
            if total >= 11: total+= 1
        
            else: total+= 11
        
        else: total += card
    
    return total

""" This function handles if the user wants to hit (draw a new card) """
def hit(hand):

    # new card is drawn
    card = deck.pop()

    # Naming the numered cards their proper card names
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"

    # card is added to the hand
    hand.append(card)
    return hand


""" Function that clears the terminal """
def clear():

    # all depending on if the user is using NT or POSIX operative system interface,
    # it uses either CLS or clear to clean the terminal
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


""" Function that handles the scoring system (and makes it look fancy!) """
def print_results(dealer_hand, player_hand):

    clear()

    # scoring system for wins and losses
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    
    # scoring system for money
    print("-"*30+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


""" Function to handle anybody who gets a blackjack """
def blackjack(dealer_hand, player_hand):
    
    global wins
    global losses
    global bank
    global winnings
    global bet

    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("You got a Blackjack!\n")
        wins += 1

        # bet times 1.5 is returned due to the rules that say
        # if you get a blackjack your winnings times 1.5 of your bet is given
        bank += bet *1.5
        winnings += bet *1.5
        play_again()

    elif total(dealer_hand) == 21:

        print_results(dealer_hand, player_hand)
        print ("You lose. The dealer got a blackjack.\n")
        losses += 1
        bank -= bet
        winnings -= bet
        play_again()


""" Function to handle anybody who gets a blackjack """

def score(dealer_hand, player_hand):
    
    # score function written global win/loss variables
    
    global wins
    global losses
    global bank
    global winnings
    global bet
    
    if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("You got a Blackjack!\n")
            wins += 1
            bank += bet * 1.5
            winnings += bet * 1.5
    elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("You lose. The dealer got a blackjack.\n")
            losses += 1
            bank -= bet
            winnings -= bet
    elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("You busted. You lose.\n")
            losses += 1
            bank -= bet
            winnings -= bet
    elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Dealer busts. You win!\n")
            wins += 1
            bank += bet
            winnings += bet
    elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Your score isn't higher than the dealer. You lose.\n")
            losses += 1
            bank -= bet
            winnings -= bet
    elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Your score is higher than the dealer. You win!\n")
            wins += 1
            bank += bet
            winnings += bet

""" Now we use all the functions we made and use them in the game function """
def game():
    global wins
    global losses
    global bank
    global winnings
    global bet

    choice = 0
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print("    \033[1;32;40mBANK:  \033[1;37;40m%s   \033[1;31;40mWINNINGS:  \033[1;37;40m%s\n" % (bank, winnings))
    print("-"*30+"\n")
    
    dealer_hand = deal(deck)
    player_hand = deal(deck)


    bet = int(input("How much do you want to bet?: "))

    print ("The dealer is showing a " + str(dealer_hand[0]))

    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))


    blackjack(dealer_hand, player_hand)

    quit = False

    while not quit:
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':

            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))

            # Checks if the user input is a positive number
            while True:
                try:
                    bet += int(input("How much do you want to bet?: "))
                    if bet <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("The number was not positive, please try again.")

            if total(player_hand)>21:
                print('You busted')
                losses += 1
                bank -= bet
                winnings -= bet
                play_again()

        elif choice== 's':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Dealer busts, you win!')
                    wins += 1
                    bank += bet
                    winnings += bet
                    play_again()

            score(dealer_hand,player_hand)
            play_again()

        elif choice == "q":
            print("Bye!")
            quit = True
            exit()

""" excecute the program """
if __name__ == "__main__":
   game()
