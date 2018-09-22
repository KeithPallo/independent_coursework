# Uses python3
import sys
from decimal import Decimal

def lcm_euclid(a, b):
    long = max([a,b])
    short = min([a,b])

    while True:
        mod_test = long % short

        if mod_test == 0:
            gcf = short
            break

        long = short
        short = mod_test

    lcm =((Decimal(a)*Decimal(b))/Decimal(gcf))

    return lcm

#def lcm_naive(a, b):
#    for l in range(1, a*b + 1):
#        if l % a == 0 and l % b == 0:
#            return l

#    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_euclid(a, b))
#    print(lcm_naive(a, b))

