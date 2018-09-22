# Prints the number of times a substring appears in string 's'
# The target substring is "bob"


# Defines a string 's'
s = 'pobboboobobbobobbbobobbobbbybx'


# Creates a substring to search for within larger string 's'
find = 'bob'

# Function to count the number of times a substring appears in a string
def count_substring(string, sub_string):

    length = len(string)
    counter = 0
    for i in range(length):
        for j in range(length):
            if string[i:j+1] == sub_string:
                counter +=1
    return counter

# Prints the number of times the desired substring appears
print(count_substring(s, find))
