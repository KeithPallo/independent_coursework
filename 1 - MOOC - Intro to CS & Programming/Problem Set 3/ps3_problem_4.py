# Import all prior created functions in the current directory

from ps3_problem_1 import isWordGuessed
from ps3_problem_2 import getGuessedWord
from ps3_problem_3 import getAvailableLetters

# Define final function, hangman, which will play the classic hangman game based on a secret word

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, lets the user know how many
      letters the secretWord contains.

    * Then, the script asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round,the user the sees what the partially
     guessed word so far looks like so far, as well as letters that the
      user has not yet guessed.
    '''

    # Import string module to create s list of available letters

    import string
    availableLetters = string.ascii_lowercase

    # Initialize additional constants

    lettersGuessed = []  # Empty list to hold guessed letters
    guesses = 8  # Number of guesses that the player has to guess the secret word
    word_length = len(secretWord)  # Create a variable to determine the length of the secret word
    viewers_word = '_' * word_length  # Create an initial viewer word, which is simply a string of underscores

    # Print out starting statement

    print('Welcome to the game, Hangman!')
    print()
    print('I am thinking of a words that is {} letters long'.format(word_length))

    # Loop until the user has exhausted all guesses
    while guesses > 0:

        # Initial loop statement to alert user of current game information

        print('-----------')
        print('You have {} guesses left'.format(guesses))
        print("Available letters: {}".format(availableLetters))

        # Request a guess
        print('Please guess a letter: ',end = '')

        # Allow user to input guess
        cur_guess = input()
        cur_guess = cur_guess.lower()

        # First check to see if letter is available.
        if cur_guess in availableLetters:

            # If available, check if the letter is in the secret word

            # If the letter is in the secret word, do the following:
            if cur_guess in secretWord:
                # Update the guessed word
                lettersGuessed.append(cur_guess)

                # Check to see if the secret word is guessed
                Correct = isWordGuessed(secretWord, lettersGuessed)

                # If it is guessed, update guesses to exit the loop  and set guesses to "correct" value
                if Correct == True:
                    guesses = -10

                # Update the available letters
                availableLetters = getAvailableLetters(lettersGuessed)

                # Update the viewer word
                viewers_word = getGuessedWord(secretWord, lettersGuessed)

                # Update the player
                print('Good guess: {}'.format(viewers_word))

            # If the letter is not in the secret word, do the following:
            else:
                # Update the guessed word
                lettersGuessed.append(cur_guess)

                # Decrease remaining guesses by 1
                guesses -= 1

                # Update the available letters
                availableLetters = getAvailableLetters(lettersGuessed)

                # Update the player
                print('Oops! That letter is not in my word: {}'.format(viewers_word))

        # Else function to let the user know that the guess they have just entered is not valid

        else:
            print('Oops! You\'ve already guessed that letter: {}'.format(viewers_word))

    print('-----------')

    # Check to see if the user won the game, and update accordingly

    if guesses == -10:
        print("Congratulations, you won!")

    if guesses == 0:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))

# -----------------------------------------------------------------------------------------------------

# Small script to play the game


secretWord = 'northwestern'  # Initialize the secret word

hangman(secretWord)  # Play the game



