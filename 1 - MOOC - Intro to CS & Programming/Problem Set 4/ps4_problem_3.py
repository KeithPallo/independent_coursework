def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    # Create a copy of the current hand

    hand_check = dict(hand)

    # Check to see if the word is valid. Return false if the word is not valid as defined in the words.txt file.

    if (word in wordList) == False:
        return False

    # Using the built in .get operator on a dictionary, check to see if each letter is in the current hand

    for i in range(len(word)):

        if hand_check.get((word[i]), 'not') == 'not':  # Immediately return false if any letter in word is not in hand
            return False

        # If the letter is in the hand, decrease the number of times the letter is in the current hand by 1
        hand_check[word[i]] = hand_check[word[i]] - 1

        # If the number of any letter becomes negative, return false. This means that multiple of the same
        # letter were input, and the number required to spell the word was not available in the current hand
        if hand_check.get(word[i]) < 0:
            return False

    return True

