# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    current_weight = 0

    list = []
    # Greedy Solution: Take as much as possible of the bag with the highest value / unit. In this case it
    # is the bag with the highest value / weight.

    for i in range(0,len(weights)):
        list.append([i,values[i]/weights[i]])

    list.sort(key = lambda x: x[1], reverse = True)



    for i in range(0,len(weights)):
        current_pointer = int(list[i][0])

        if weights[current_pointer] + current_weight <= capacity:
            value += values[current_pointer]
            current_weight += weights[current_pointer]


        else:
            fraction = (capacity - current_weight)/weights[current_pointer]
            value += values[current_pointer] * fraction
            current_weight += weights[current_pointer] * fraction
            break


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
