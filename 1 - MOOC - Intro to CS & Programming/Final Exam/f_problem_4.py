def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    # Create an empty list
    max_list = []

    # For all in the tuple or list
    for i in range(len(t)):

        # Check to see if the value is an integer
        if type(t[i]) == int:
            # If it is, append it
            max_list.append(t[i])

        else:
            # If not, recursively call max_val to append all sub elements
            max_list.append(max_val(t[i]))

    return max(max_list)
