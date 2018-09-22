# Uses python3
import sys

def get_change(money):
    # Set value of coins matrix
    coins = [4,3,1]

    # Set all min values to 0 in a list that has money + 1 values. This is because
    # there must be a 0th case, which corresponds to index 0.
    min = [0] * (money+1)

    # Excluding the first value of 0, do the following:

    for m in range(1,len(min)):
        # Set the current value to some impossible value. We know the number of coins
        # will be less than this value

        min[m] = 1000000

        # Check the following for each coin:
        for i in range(0,len(coins)):

            # If the index is greater than the coin value
            if m >= coins[i]:
                # Determine the number of coins that would be created by adding
                # the current coin with the designated value. This is the number of coins
                # at index m - value + 1
                numcoins = min[m-coins[i]] + 1

                # Check to see if this is the min number possible for all coins
                # that have been tried so far. This loop will run for all viable
                # coins, so it will automatically calculate the min number based off
                # of value
                if numcoins < min[m]:
                    min[m] = numcoins

    #print(min)
    return min[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
