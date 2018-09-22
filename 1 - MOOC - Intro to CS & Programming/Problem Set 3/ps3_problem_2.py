# Function to display the correct "guessed" representation to the player. I.E. - if letters are guessed correctly,
# then they are displayed instead of having an underscore

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    # Initialize a variable to hold the previous secret word representation
    original = secretWord

    # For each letter in the string lettersGuessed, if the letter is in the secretWord, replace all
    # occurrences in the secret word with an underscore

    for i in range(0, len(lettersGuessed)):
        cur_letter = lettersGuessed[i]
        if cur_letter in secretWord:
            secretWord = secretWord.replace(cur_letter, "_")

    # Create an empty list called answer
    answer = []

    # Essentially create a "reverse" or "mirror" image of the current secret word variable. For every
    # underscore replace the original letter, and for every letter, replace with an underscore

    for i in range(0, len(secretWord)):
        if secretWord[i] == '_':
            answer.append(original[i])
        else:
            answer.append('_')

    # Return the final version that the player will see

    final = ''.join(answer)
    return (final)