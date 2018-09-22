# python3

import sys
from collections import deque


def createGroups(v, visited, adj, counter, groups):

    if counter not in visited:
        visited[counter] = {}

    if v not in visited[counter]:
        visited[counter][v] = counter
        if len(groups) == counter:
            groups.append([])
        groups[counter].append(v)
        for a in adj[v]:
            if a not in visited[counter]:
                createGroups(a, visited, adj, counter, groups)
        counter += 1
    else:
        for a in adj[v]:
            if a not in visited[counter]:
                createGroups(a, visited, adj, counter, groups)

    return counter


# searches for all reachable vertices from v, following an adjacency list
def explore(v, visited, adj, counter, groupStart):
    if v not in visited:
        visited[v] = counter

        for a in adj[v]:
            if a not in visited:
                explore(a, visited, adj, counter, groupStart)
        groupStart[counter] = v
        counter += 1
    else:
        for a in adj[v]:
            if a not in visited:
                explore(a, visited, adj, counter, groupStart)


    return counter


def relax(u, v, w, dist, prev):
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        prev[v] = u


def bellmanFord(V, E, s):
    dist = [float('inf')] * V
    prev = [None] * V
    dist[s] = 0

    for i in range(V):
        for edge in E:
            relax(edge[0], edge[1], edge[2], dist, prev)

    for e in E:
        u = e[0]
        v = e[1]
        w = e[2]
        print(u,v,w)
        if dist[u] + w < dist[v]:
            return 1

    return 0


def negative_cycles(adj, E):
    visited = {}
    counter = 0
    groupStart = {}
    groups = []

    for v in range(len(adj)):
        counter = explore(v, visited, adj, counter, groupStart)

    print(groupStart[1])

    if counter == 1:
        return bellmanFord(len(adj), E, 0)

    else:
        c = 0
        while c < counter:
            if bellmanFord(len(adj), E, groupStart[c]) == 1:
                return 1
            c += 1

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
    for e in edges:
        edg.append([e[0][0] - 1, e[0][1] - 1, e[1]])

    print(negative_cycles(adj, edg))

