from ps4a import *
from ps4_problem_1 import *
from ps4_problem_2 import *
from ps4_problem_3 import *
from ps4_problem_4 import *
from ps4_problem_5 import *

# When script is run, the game will start


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """

    n = HAND_SIZE
    num_runs = 0
    end = False
    okay = ['n', 'r', 'e']

    # Repeat the following as long as end is equal to false

    while end == False:

        # Ask user for input
        print('Enter n to deal a new hand, r to replay the last hand, or e to end game: ', end='')

        user_input = input()

        # Perform action based on description of function. Additional comments on Problem 7.

        if (user_input in okay) == True:
            if num_runs == 0 and user_input == 'r':
                print('You have not played a hand yet. Please play a new hand first!')
                print('')

            elif user_input == 'r' and not num_runs == 0:
                playHand(hand, wordList, n)
                print('')
                num_runs += 1

            elif user_input == 'n':
                hand = dealHand(n)
                playHand(hand, wordList, n)
                print('')
                num_runs += 1
            elif user_input == 'e':
                end = True

        # Account for other inputs

        else:
            print('Invalid command.')


x = playGame(loadWords())