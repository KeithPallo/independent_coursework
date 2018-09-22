# python3


import sys
import copy


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def adjust(seq, n):
    for x in range(len(seq)):
        for i in range(len(seq[x])):
            seq[x][i] = seq[x][i] - n
            if seq[x][i] < 0:
                seq[x][i] = seq[x][i] + len(seq)

    return seq

class explorer:

    def __init__(self,visited,adj):
        self.test = False
        self.visited = visited
        self.adj = adj

    def explore(self,x):

        self.visited[x] = True

        for i in range(len(self.adj[x])):
            current = self.adj[x][i]

            if self.visited[current] == False:
                self.explore(current)


def relax(u, v, w, dist, prev):
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        prev[v] = u


def bellmanFord(V, E, s):

    dist = [100000000000000] * V
    prev = [None] * V
    dist[s] = 0

    for i in range(V-1):
        for edge in E:
            relax(edge[0], edge[1], edge[2], dist, prev)

    for e in E:
        u = e[0]
        v = e[1]
        w = e[2]

        if dist[u] + w < dist[v]:
            return 1

    return 0


def negative_cycle(adj, E):


    visited = [False for _ in range(len(adj))]

    test = explorer(visited, adj)
    test.explore(0)
    visited = test.visited

    if bellmanFord(len(adj), E, 0) == 1:
        return 1

    while False in visited:
        first = visited.index(False)

        test = explorer(visited, adj)
        test.explore(first)
        visited = test.visited

        if bellmanFord(len(adj), E, first) == 1:
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    edg = []
    contains_negative = False
    for e in edges:
        edg.append([e[0][0] - 1, e[0][1] - 1, e[1]])
        if e[1] < 0:
            contains_negative = True

    if contains_negative == True:
        print(negative_cycle(adj, edg))

    else:
        print(0)

