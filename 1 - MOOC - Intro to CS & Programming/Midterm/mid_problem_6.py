def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """

    # Initialize two empty lists

    output_odd_only = []
    output_even_only = []

    # For every letter, check to see if odd or even and append to the appropriate list

    for i in range(len(L)):
        count = L.count(L[i])
        if count % 2 == 0:
            output_even_only.append(L[i])
        else:
            output_odd_only.append(L[i])

    # Check to see if the odd only list is empty - if so return none

    if not output_odd_only:
        return None

    # Using the built in max list operator, return the max int

    return (max(output_odd_only))