# Uses python3

def edit_distance(s, t):

    # Create and initialize the grid matrix appropriately
    grid = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

    for i in range(0,len(s)+1):
        grid[i][0] = i

    for j in range(0,len(t)+1):
        grid[0][j] = j

    # For all values, calculate the optimal move.
    for j in range(1,len(t)+1):
        for i in range(1,len(s)+1):
            #print(i,j)
            insertion = grid[i][j-1]+1
            deletion = grid[i-1][j]+1
            match = grid[i-1][j-1]
            mismatch = grid[i - 1][j - 1] + 1 n
            if s[i-1] == t[j-1]:
                grid[i][j] = min(insertion,deletion,match)
            else:
                grid[i][j] = min(insertion, deletion, mismatch)


    return grid[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
