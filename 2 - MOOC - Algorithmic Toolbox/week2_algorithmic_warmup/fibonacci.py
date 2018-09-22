# Uses python3
import random

# Create a function to compute the nth Fibonachi number that is efficient.

def calc_fib(n):

    # Create a list that is as long as the input number

    if n == 0:
        return 0


    elif n == 1:
        return 1

    else:

        fib_table = [None] * (n + 1)


        fib_table[0] = 0
        fib_table[1] = 1


        for i in range(2,n+1):
            fib_table[i] = fib_table[i-1] + fib_table[i-2]

        return fib_table[n]

n = int(input())
print(calc_fib(n))



# Test Module
# ----------------------------------------

#for x in range(10):
#    i = random.randint(0,45)
#    print(i)
#    print(calc_fib(i))



