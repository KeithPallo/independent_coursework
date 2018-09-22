# Function to see what letters are available based upon the letters that
# have been guessed so far

def getAvailableLetters(lettersGuessed):

    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Import the string module
    import string

    # Create an available string which contains all lowercase letters
    available = string.ascii_lowercase

    # Remove all letters in the string "letters guessed" and return the available letters
    for i in range(0, len(lettersGuessed)):
        cur_letter = lettersGuessed[i]
        if cur_letter in available:
            available = available.replace(cur_letter, "")

    return available 