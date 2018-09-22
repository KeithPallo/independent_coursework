# Uses python3

def eval(a,b,op):


     if op == '+':
        return a + b
     elif op == '-':
        return a - b
     elif op == '*':
        return a * b
     else:
        assert False


def min_max(i,j,opps,m,M):

    i = i - 1
    j = j - 1

    min_val =  100000000
    max_val = -100000000

    for x in range(i,j):
        a = eval( M[i][x] ,M[x+1][j] ,opps[x])
        b = eval( M[i][x] ,m[x+1][j] ,opps[x])
        c = eval( m[i][x] ,M[x+1][j] ,opps[x])
        d = eval( m[i][x] ,m[x+1][j] ,opps[x])



        min_val = min(min_val,a,b,c,d)
        max_val = max(max_val,a,b,c,d)

    return[min_val,max_val]


def get_maximum_value(dataset):
    #write your code here
    determinant = len(dataset)

    if determinant == 1:
        return int(dataset)

    if determinant == 0:
        return 0

    num_of_ops = (determinant // 2)

    num_of_digits = num_of_ops + 1

    m = [[0 for i in range(num_of_digits)] for j in range(num_of_digits)]
    M = [[0 for i in range(num_of_digits)] for j in range(num_of_digits)]



    opps = []
    digits = []

    for i in range(0, determinant, 2):

        m[(i//2)][(i//2)] = int(dataset[i])
        M[(i//2)][(i//2)] = int(dataset[i])

    for i in range(1,determinant,2):
        opps.append(dataset[i])


    for s in range(1,num_of_digits+1):
        for i in range(1,1+num_of_digits-s):
            j = i + s

            x = min_max(i,j,opps,m,M)
            x_1 = x[1]
            x_2 = x[0]

            M[i-1][j-1] = x_1
            m[i-1][j-1] = x[0]


            max = x[1]


    return max

if __name__ == "__main__":
    print(get_maximum_value(input()))
