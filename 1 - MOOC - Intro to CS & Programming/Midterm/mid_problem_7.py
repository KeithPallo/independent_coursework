def dict_invert(d):
    '''
    d: dict

    Takes in a dictionary with immutable values and returns the inverse of the dictionary.
    The inverse is another dictionary whose keys are the unique dictionary values in the input dictionary d.
    The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d
    that have the same value in d.

    '''

    # Initialize variables

    output = {}  # Create a new empty dictionary
    keys = list((d.keys()))  # Determine the keys of the input dictionary

    # For all keys do the following:
    for i in range(len(keys)):

        # Check to see if the input dictionary value associated with the current index is in the output keys.
        # Essentially, check to see if, for one of the values from the input dictionary, there is an associated key.

        if ((d[keys[i]] in list((output.keys())))) == True:

            # If there is, append the value from the input dictionary to the output
            output[d[keys[i]]].append(keys[i])

            # Find the correct list
            int = (output[d[keys[i]]])

            # Sort the list
            fix = sorted(int)

            # Update the output dictionary keys appropriately
            output.update({d[keys[i]] : fix})

        # If the criteria is not met, update the output matrix accordingly

        else:
            output.update({d[keys[i]] : [keys[i]]})

    return(output)
