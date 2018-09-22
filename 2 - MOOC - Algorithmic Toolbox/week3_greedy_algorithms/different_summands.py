# Uses python3
import sys

def optimal_summands(n):
    summands = []
    increment = 1
    total = 0

    if n == 1:
        summands.append(1)
        return summands

    if n == 2:
        summands.append(2)
        return summands

    while True:
        total += increment
        summands.append(increment)
        if n < (total + (increment+1) + (increment+2)):
            last_int = n - total
            summands.append((last_int))
            total += last_int
            break
        else:
            increment +=1


    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
