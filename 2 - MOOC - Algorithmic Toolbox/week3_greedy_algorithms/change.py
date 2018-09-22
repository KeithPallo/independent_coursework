# Uses python3
import sys

def get_change(m):
    coins = []
    remaining_change = m
    # Greedy choice will be to keep taking as many large coins as possible

    coins.append(remaining_change // 10)

    current_dollar = coins[0] * 10

    remaining_change -= current_dollar

    coins.append(remaining_change // 5)

    current_dollar += coins[1] * 5


    coins.append(m - current_dollar)

    return sum(coins)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
