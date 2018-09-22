# Uses python3
import sys

def get_majority_element(a, left, right):

    if len(a) == 1:
        return a[0]

    dict = {}

    for i in range(left,right):
        current = dict.get(a[i])

        if current == None:
            dict.update({a[i]:1})

        else:

            new = dict.get(a[i]) + 1

            if new > (right/2):
                return 1
                break

            else:
                dict.update({a[i]:new})

    return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
