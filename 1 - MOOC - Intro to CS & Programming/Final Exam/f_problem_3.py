def sum_digits(s):
    import re
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """

    # Initialize count and integer values to be 0
    int_sum = 0
    count_int = 0

    # For all characters in s, check to see if it is an integer
    # If it is, increment the count of integers (count_int) by 1
    # and increment the integer sum (int_count) by the arropriate value

    for i in range(len(s)):
        if s[i].isdigit() == True:
            int_sum += int(s[i])
            count_int += 1

    # Check to see that there was at least one integer. Return an error
    # if there were none, if not, return the sum of all the integers

    if count_int == 0:
        raise ValueError
    else:
        return int_sum
