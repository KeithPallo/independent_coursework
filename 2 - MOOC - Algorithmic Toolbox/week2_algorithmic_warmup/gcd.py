# Uses python3
import sys

def gcd_eclud(a,b):
    long = max([a,b])
    short = min([a,b])

    while True:
        mod_test = long % short

        if mod_test == 0:
            return short

        long = short
        short = mod_test


#def gcd_naive(a, b):
#    current_gcd = 1
#    for d in range(2, min(a, b) + 1):
#        if a % d == 0 and b % d == 0:
#            if d > current_gcd:
#                current_gcd = d

 #   return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_eclud(a, b))

