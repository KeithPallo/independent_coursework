# Prints the longest alphabetical substring in a string 's'

# Test string is defined

s = 'vckourwfhyvqxv'


# Function to find the longest alphabetical substring
def longest_alpha(string):

    # Initialize first letter list
    letter = s[0]

    # Initialize an empty string
    current_best = ''

    for i in range(1 , len(string)):

        # For loop to iterate through all characters. If the current letter is greater in comparison (in order)
        # add the letter to the current letter list. If not, reset the letter list.
        # Then compare the len of the letter list to the current "best". If it is the best, reset the variable
        # current best. Iterate through all instances

        if s[i] >= s[i-1]:
            letter += s[i]
        else:
            letter = s[i]
        if len(letter) > len(current_best):
            current_best = letter

    final_best = current_best

    # Since there are no ordered characters, we choose the first character
    if len(final_best) == 1:
        final_best = s[0]

    return(final_best)

# Prints desired output
print(longest_alpha(s))