#Uses python3

import sys


def greater_check(digit_1, digit_2):


    digit_1_cat = digit_1 + digit_2
    digit_2_cat = digit_2 + digit_1

    if int(digit_1_cat) >= int(digit_2_cat):
        return True

    else:
        return False


def largest_number(a):
    sorted = ''

    while len(a) > 0:
        maxdigit = ''
        for i in range(0,len(a)):
            if greater_check(a[i],maxdigit) is True:
                maxdigit = a[i]
        sorted = sorted + maxdigit
        a.remove(maxdigit)

    return sorted






if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
