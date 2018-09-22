# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    i = l
    j = l
    k = r



    while j <= k:

        if a[j] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1

        elif a[j] == x:
            j += 1

        elif a[j] > x:
            a[j], a[k] = a[k], a[j]
            k -=1


    list_of_pointers = [i,j]

    return list_of_pointers


    j = r;
    gt = r
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    output_locations = partition3(a,l,r)

    randomized_quick_sort(a, l, output_locations[0]-1);

    randomized_quick_sort(a, output_locations[1], r);



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

