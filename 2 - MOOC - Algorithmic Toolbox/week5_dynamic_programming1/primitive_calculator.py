# Uses python3
import sys


def optimal_sequence(n):
    v = [0] * (n + 1)  # Create a list that has 0's for all values and is len n+1

    # This list will contain the number of optimal operations to arrive at the value equal to the index of v.
    # For example, v[4] will contain the optimal number of operations to arrive at the number 4. Hence, the list
    # must be of length n+1 in order to make v[n] a viable option.

    # Sequence list is the output list
    sequence = []

    v[1] = 1  # Set trivial value of 1

    for i in range(1, n + 1):  # For all remaining values in the sequence

        # This portion finds the minimum next step

        # Set the current value to the last index + 1. This represents the least
        # productive operation in terms of scaling upwards to bigger numbers,
        # so in essence, it is the worst option if any others are viable.
        v[i] = v[i - 1] + 1

        # Check to see if the current index is divisible by 2
        if (i % 2) == 0:
            # If it is, we need to see if it would be optimal to have multiplied the n //2
            # by 2 as opposed to adding 1 to the number at the previous index. We do this by
            # taking the min number the two options

            v[i] = min((1 + v[i // 2]), v[i])

        # The same process is repeated for numbers divisible by 3.
        if (i % 3) == 0:
            v[i] = min((1 + v[i // 3]), v[i])

    # Now we create the output by "backtracking" through matrix v.

    while n > 1:

        # Append the current number
        sequence.append(n)

        # Check to see if the previous number indicates that a 1 was added. If so, decrement n by 1.
        if v[n - 1] == v[n] - 1:
            n = n - 1

        # Check to see if the current n is divisible by 3. If it is, check to see if the value at v[n // 3] is
        # only 1 less than the value at v[i]. This indicates a multiplication of 3 was optimal.
        elif (n % 3) == 0 and v[n // 3] == v[n] - 1:
            n = n // 3

        # Repeat for 2. This must be an elif, because numbers divisible by 6 are divisible by 3 and 2.
        elif (n % 2) == 0 and v[n // 2] == v[n] - 1:
            n = n // 2

    sequence.append(1)

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
