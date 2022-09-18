#! python 3

"""Carrot in a Box, by Al Sweigart al@inventwithpython.com
A silly bluffing game between two human players. Based on the game
from the show 8 Out of 10 Cats.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, game, two-player"""

import random
print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')

playAgain = 'Y'
p1Score = 0
p2Score = 0
p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

while playAgain.startswith('Y'):
    input('Press Enter to begin...')

    print('''HERE ARE TWO BOXES:
       __________    __________
      /         /|  /         /|
     +---------+ | +---------+ |
     |   RED   | | |  GOLD   | |
     |   BOX   | / |  BOX    | /
     +---------+/  +---------+/''')

    print()
    print("     " + playerNames)
    print()
    print(p1Name + ', you have a RED box in front of you.')
    print(p2Name + ', you have a GOLD box in front of you.')
    print()
    print(p1Name + ', you will get to look into your box.')
    print(p2Name.upper() + ', close your eyes and don\'t look!!!')
    input('When ' + p2Name + ' has closed their eyes, press Enter...')
    print()

    print(p1Name + ' here is the inside of your box:')

    if random.randint(1, 2) == 1:
        carrotInFirstBox = True
    else:
        carrotInFirstBox = False

    if carrotInFirstBox:
        print('''
       ___VV____
      |   VV    |
      |   VV    |
      |___||____|      __________
     /    ||    /|   /         /|
     +---------+ |  +---------+ |
     |   RED   | |  |   GOLD  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/
     (carrot!)''')
    else:
        print('''
       _________
      |         |
      |         |
      |_________|      __________
     /          /|   /         /|
     +---------+ |  +---------+ |
     |   RED   | |  |   GOLD  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/
     (no carrot!)''')
        print("     " + playerNames)

    input("Press Enter to continue...")

    print('\n' * 100) # Clear the screen by printing several newlines.
    print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
    input('Press Enter to continue...')

    print()
    print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
    print(' 1) There is a carrot in my box.')
    print(' 2) There is not a carrot in my box.')
    print()
    input('Then press Enter to continue...')

    print()
    print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
    while True:
        response = input("> ").upper()
        if not (response.startswith('Y') or response.startswith('N')):
            print(p2Name + ", Please enter 'YES' or 'NO'")
        else:
            break

    firstBox = 'RED ' # Note the space after the'D'/
    secondBox = 'GOLD'

    if response.startswith('Y'):
        carrotInFirstBox = not carrotInFirstBox
        firstBox, secondBox = secondBox, firstBox

    print('''HERE ARE THE TWO BOXES:
      __________    __________
     /         /|  /         /|
    +---------+ | +---------+ |
    |   {}  | | |   {}  | |
    |   BOX   | / |   BOX   | /
    +---------+/  +---------+/'''.format(firstBox, secondBox))
    print("     " + playerNames)

    input('Press Enter to reveal the winner...')
    print()

    if carrotInFirstBox:
        print('''
       ___VV____    _________
      |   VV    |  |         |
      |   VV    |  |         |
      |___||____|  |_________|
     /    ||   /| /          /|
    +---------+ | +---------+ |
    |   {}  | | |   {}  | |
    |   BOX   | / |   BOX   | /
    +---------+/  +---------+/'''.format(firstBox, secondBox))

    else:
        print('''
       _________    ___VV____
      |         |  |   VV    |
      |         |  |   VV    |
      |_________|  |___||____|
     /         /| /    ||    /|
    +---------+ | +---------+ |
    |   {}  | | |   {}  | |
    |   BOX   | / |   BOX   | /
    +---------+/  +---------+/'''.format(firstBox, secondBox))

    print("     " + playerNames)

    # This modification made possible through the 'carrotInFirstBox' variable
    if carrotInFirstBox:
        print(p1Name + ' is the winner!')
        p1Score += 1
    else:
        print(p2Name + ' is the winner!')
        p2Score += 1

    print("Scores are: " + str(p1Score) + " for " + p1Name + " and " + str(p2Score) + " for " + p2Name)

    print("Would you like to play again? YES/NO")
    while True:
        playAgain = input("> ").upper()
        if not (playAgain.startswith('Y') or playAgain.startswith('N')):
            print("Please enter 'YES' or 'NO'")
        else:
            break

print('Thanks for playing!')