from ps4a import *
from ps4_problem_1 import *
from ps4_problem_2 import *
from ps4_problem_3 import *

def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """

    # Create a copy of the current hand dictionary

    sum_dict = dict(hand)

    # Create a sum based on the number of values, by using the dictionary operator sum

    total_letters = sum(sum_dict.values())

    return total_letters
