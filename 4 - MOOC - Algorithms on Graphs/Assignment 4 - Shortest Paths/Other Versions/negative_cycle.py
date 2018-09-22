#Uses python3

import sys
import copy
import time

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


def Bellman_ford(adj,cost):



    dist = [99999 for _ in range(len(adj))]
    prev = [False for _ in range(len(adj))]

    dist[0] = 0

    for x in range(len(adj)):
        for i in range(len(adj[x])):
            dist_before = copy.deepcopy(dist)
            v = adj[x][i]
            if dist[v] > dist[x] + cost[x][i]:
                dist[v] = dist[x] + cost[x][i]
                prev[v] = x

    print(dist_before,dist)

    if dist_before == dist:
        return 0,0,0

    return prev,v,dist

def negative_cycle(adj, cost):




    visited = [False for _ in range(len(adj))]

    test = explorer(visited, adj)
    test.explore(0)
    visited = test.visited

    dist=[float('inf')]*len(adj)
    dist[0] = 0
    #print(adj)


    for i in range(len(adj)):

        for u in range(len(adj)):


            for v in adj[u]:
                v_index = adj[u].index(v)

                if dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    if i == len(adj) - 1:
                        return 1

    i = 0

    #print(visited)
    while False in visited:

        i = i + 1

        if i > 1000:
            break


        first = visited.index(False)

        #print(visited)
        adj = shift(adj,first)
        adj = adjust(adj,first)
        cost = shift(cost,first)
        visited = shift(visited,first)

        test = explorer(visited, adj)
        test.explore(0)
        visited = test.visited

        dist = [float('inf')] * len(adj)
        dist[0] = 0


        for i in range(len(adj)):

            for u in range(len(adj)):
                for v in adj[u]:
                    v_index = adj[u].index(v)

                    if dist[v] > dist[u] + cost[u][v_index]:
                        dist[v] = dist[u] + cost[u][v_index]
                        #visited[v] = True
                        if i == len(adj) - 1:
                            return 1


    return 0


    #hash_check = {}
    #prev_lookup, search_node,dist = Bellman_ford(adj, cost)

    #if (prev_lookup and search_node and dist) == 0:
#        return 0

    #sum = 0
    #for i in range(len(adj)):

     #   if i == 0:
      #      hash_check[prev_lookup[search_node]] = "inserted"
       #     search_node = prev_lookup[search_node]

        #if prev_lookup[search_node] in hash_check.keys():
         #   cycle = 1
          #  break

        #else:
         #   hash_check[prev_lookup[search_node]] = "inserted"
          #  search_node = prev_lookup[search_node]
           # sum = sum + dist[search_node] - dist[prev_lookup[search_node]]


    #if cycle == 1 and sum < 0:
     #   return 1

    #return 0


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
    print(negative_cycle(adj, cost))
