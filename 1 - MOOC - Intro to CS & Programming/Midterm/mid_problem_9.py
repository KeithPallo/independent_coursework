def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''

    # Check to see if lengths are the same. They must be the same in order to be a permutation

    if ( len(L1) == len(L2) ) == False:
        return False

    # Check to see if both strings are empty - if so, return all None values

    if (len(L1) + len(L2)) == 0:
        return (None, None, None)

    # Initialize count and max value terms

    max_count = 0
    max_value = 0

    # For each letter of L1, do the following:
    for i in range(len(L1)):

        # Set the L1 value to be the integer at this index
        L1_value = L1[i]

        # Find the number of times the letter occurs in each string
        L1_count = L1.count(L1_value)
        L2_count = L2.count(L1_value)

        # Make sure the strings are permutations by making sure the count of each integer is the same in each string
        # Return false if this is not the case
        if (L1_count == L2_count) == False:
            return False

        # If strings are in fact meeting the permutation criteria, check to see if the index is the most frequent letter
        # If so, reset the max value
        if (L1_count > max_count) == True:
            max_count = L1_count
            max_value = L1_value

    # Return the outputs
    return (max_value,max_count, type(max_value))
