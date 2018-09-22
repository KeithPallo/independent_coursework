# Uses python3
import sys

def optimal_weight(W, weights):


    dynamic_grid = [[0 for j in range(W + 1)] for i in range(len(weights) + 1)]

    for i in range(1,len(weights)+1):

        for w in range(1,W+1):
            #print(i,w)
            dynamic_grid[i][w] = dynamic_grid[i-1][w]

            if weights[i-1] <= w:
                value = dynamic_grid[i-1][w-weights[i-1]] + weights[i-1]
                if dynamic_grid[i][w] < value:
                    dynamic_grid[i][w] = value

    #print(dynamic_grid)
    return dynamic_grid[len(weights)][W]

    # Naive algorithm
    result = 0
    #for x in w:
    #    if result + x <= W:
    #        result = result + x
    #return dynamic_grid

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
