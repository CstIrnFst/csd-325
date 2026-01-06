# Nathan J. Maurer
# December 21, 2025
# Assignment 3.2
# Advanced Python



"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.  If a player rolls a
2 or 7 on their turn, they will earn a 10 mon bonus.
''')        # If 2 or 7 is rolled, player gets a 10 mon bonus.

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        njm = input('> ')
        if njm.upper() == 'QUIT':       # Change input prompt to initials
            print('Thanks for playing!')
            sys.exit()
        elif not njm.isdecimal():
            print('Please enter a number.')
        elif int(njm) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            njm = int(njm)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display bonus if 2 or 7 is rolled and specify what was rolled:
    if dice1 + dice2 == 2 or dice1 + dice2 == 7:
        print('The dealer rolled a', dice1 + dice2, 'so you get a 10 mon bonus!')
        playerWon = True
        njm = njm + 10  # Add the bonus to the pot.

    # Display the bet results:
    if playerWon:
        print('You won! You take', njm, 'mon.')
        purse = purse + njm  # Add the pot from player's purse.
        print('The house collects a', njm // 10, 'mon fee.')
        purse = purse - (njm // 12)  # The house fee is 12%. This is increased from 10%.
    else:
        purse = purse - njm  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
