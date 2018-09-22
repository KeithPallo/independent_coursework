#Uses python3

import sys


class graph:

    def __init__(self,adj):
        self.adj = adj
        self.visited = [ False for _ in range(len(adj))]
        self.cycle = False
        self.stack = []
        self.path = []


    def dfs_execute(self):
        for x in range(0,len(self.visited)):
            if self.visited[x] == False and self.cycle == False:
                self.dfs(x)
                self.stack.clear()



    def dfs(self,y):


        self.stack.append(y)

        self.visited[y] = True

        self.path.append(self.stack[-1]+1)


        for i in range(len(self.adj[y])):
            current = self.adj[y][i]

            if current in self.stack:
                self.cycle = True
                break

            if self.visited[current] == False:
                self.dfs(current)
            try:
                self.stack.pop()
            except:
                pass



def acyclic(adj):

    test = graph(adj)

    test.dfs_execute()

    print(test.path)

    if test.cycle == False:
        return 0

    else:
        return 1



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    print(acyclic(adj))
