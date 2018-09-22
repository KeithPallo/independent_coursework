# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):

    remainder = n % get_pisano(m)

    first = 0
    second = 1

    res = remainder

    for i in range(1,remainder):
        res = (first + second) % m
        first = second
        second = res


    return res % m

def get_pisano(n):
    a = 0
    b = 1
    c = a + b

    for i in range(0,n*n):
        c = (a + b) % m
        a = b
        b = c

        if a == 0 and b == 1:
            return i+1


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
