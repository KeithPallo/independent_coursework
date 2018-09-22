def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    # Simply use the built in replace function for all vowels, both lowercase and uppercase

    s = s.replace('a',"")
    s = s.replace('e',"")
    s = s.replace('i',"")
    s = s.replace('o',"")
    s = s.replace('u',"")
    s = s.replace('A',"")
    s = s.replace('E',"")
    s = s.replace('I',"")
    s = s.replace('O',"")
    s = s.replace('U',"")
    print(s)