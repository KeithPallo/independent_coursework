from ps4a import *
from ps4_problem_1 import *




def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    # Create a new dictionary

    hand_new = dict(hand)

    # Remove all the letters passed in from the word that are currently in the hand

    for i in range(len(word)):
        if hand_new.get((word[i]),0) > 0:
            hand_new[word[i]] = hand_new[word[i]] - 1

    return hand_new  # Return the modified dictionary