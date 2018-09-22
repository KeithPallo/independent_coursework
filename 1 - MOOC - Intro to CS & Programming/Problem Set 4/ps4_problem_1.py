from ps4a import *

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES in ps4a.py)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    # Initialize variables

    # Lower case version of the input word
    lower_word = word.lower()

    # Points for word is initially 0
    points = 0

    # For each letter in the played word, assign a value and increment total points
    for i in range(len(lower_word)):
        letter = lower_word[i]
        value = SCRABBLE_LETTER_VALUES[letter]
        points += value

    # Multiply the length of the word by the individual letter points sum, as is done in Scrabble.

    total = points * len(lower_word)

    # If all the letters in one's hand are plaid, add an additional 50 points to the total.
    # Then return the appropriate sum

    if n == len(lower_word):
        total += 50
        return total
    else:
        return total

