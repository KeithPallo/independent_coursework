def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """

    # Create an empty key_code dictionary
    key_code = {}

    # Create an empty string
    string = ''

    # For all map_from characters:
    for i in range(len(map_from)):

        # Append the map_to value to the key_code dictionary using the map_from as the key
        key_code[map_from[i]] = map_to[i]

    # Using the newly created key_code dictionary create a coded string
    for i in range(len(code)):
        string += key_code[code[i]]

    # Return the coded string
    return (key_code,string)

# Example test case is shown below

print(cipher("abcd", "dcba", "dab"))