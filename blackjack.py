#! python3

"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-of-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS  = chr(9829) # character 9829 is '♥'.
DIAMONDS = chr(9830) # character 9830 is '♦'.
SPADES  = chr(9824) # character 9824 is '♠'.
CLUBS    = chr(9827) # character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True: # Main game loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You\'re broke!")
            print("Good thing you weren't playing with real money!")
            print("Thanks for playing!")
            sys.exit()

        # Let the play enter their bet for this round:
        print("Money: ", money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        '''
        list.pop(pos)
        pos	Optional. A number specifying the position of the element you want to remove,
        default value is -1, which returns the last item.  so deck.pop() is returning
        the last cards from the deck[] list
        '''

        # Handle player actions:
        print("Bet: ", bet)
        while True:  # Keep looping until the player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has busted:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            # Handle the player's actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to ().'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break
                #print("OK. No card for you") # used to be break

        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost or tied:
        if dealerValue > 21:
            print("Dealer busts! You win ${}!".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print("You won ${}!".format(bet))
        elif playerValue == dealerValue:
            print("It\'s a tie, the bet is returned to you.")

        input("Press Enter to continue...")
        print("\n\n")

def getBet(maxBet):
    """Ask the player how much thev want to bet for this round."""
    while True: # Keep asking until they enter a valid amount.
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards as tuples (,).
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards.  Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards): # cards = playerHand or dealerHand
    """Returns the value of the cards.  Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value of the non-ace cards:
    for card in cards:
        # print("Hey Presley, card = ", str(card)) # debug
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points
            value += 10
        else:
            # print("Hey Presley, Rank = {}".format(rank)) # debug
            value += int(rank) # Numbered cards are worth their number

    # Add the value of the aces:
    value += numberOfAces # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value +10 <= 21:
                value+= 10

    return value

def displayCards(cards): # cards = dealerHand or playerHand
    """Display all the cards in the cards list."""
    rows = ['','','','',''] # The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # The top line of the card.
        if card == BACKSIDE:
            # Print the card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    # Print each row on the screen:
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True: # Keep looping until the player enters a correct one.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has entered a valid move.

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()









