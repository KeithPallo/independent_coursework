#Uses python3

import sys

def reach(adj, x, y):
    visited = [ False for _ in range(len(adj))]


    z = explorer(visited)
    z.explore(adj, x, y)

    return z.path_check(x,y)

class explorer:

    def __init__(self,visited):
        self.test = False
        self.visited = visited

    def explore(self,adj,x,y):

        self.visited[x] = True

        for i in range(len(adj[x])):
            current = adj[x][i]

            if self.visited[current] == False:
                self.explore(adj,current,y)

    def path_check(self,x,y):

        if self.visited[x] == True and self.visited[y] == True:
            return 1
        else:
            return 0




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, x, y))
