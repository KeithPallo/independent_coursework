# Prints the number of vowels in a string s.

s = 'hqnirshutkjzaemab'   # Defines a string 's'

x = 0  # Initialize number of vowels to be 0

for letter in s:          # For all letters, check to see if the current letter is a vowel.
    if letter == 'a':
        x += 1
    elif letter == 'e':
        x += 1
    elif letter == 'i':
        x += 1
    elif letter == 'o':
        x += 1
    elif letter == 'u':
        x += 1
    else:
        x = x

print(x)  # Prints the number of vowels in string 's'
