# Function to determine if the word has been guessed by the player

def isWordGuessed(secretWord, lettersGuessed):
    ''' Inputs:
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed False otherwise
    '''

    # For each letter in letters guessed input perform the following:
    for i in range (0,len(lettersGuessed)):

        # Initialize a "current" letter variable
        cur_letter = lettersGuessed[i]

        # Check to see if the letter is in the secret word
        if cur_letter in secretWord:

            # If it is, remove the letter from the secret word
            secretWord = secretWord.replace(cur_letter, "")

    # If secret word is blank, then all letters will have been guessed, and return True
    if secretWord == '':
        return True

    # Else the word is not guessed and return false
    else:
        return False


