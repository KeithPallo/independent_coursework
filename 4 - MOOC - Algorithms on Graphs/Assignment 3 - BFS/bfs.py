#Uses python3

import sys
import queue


def reconstruct_path(s, u, prev):
    result = []


    if prev[u] is False:
        return -1

    while u != s:
        result.append(u)
        u = prev[u]

    return len(result)


def distance(adj, s, t):

    dist_values = [999999 for _ in range(len(adj))]
    prev_info = [False for _ in range(len(adj))]

    dist_values[s] = 0
    prev_info[s] = "start"


    q = queue.Queue()
    q.put(s)

    while q.empty() != True:
        u = q.get()
        for i in range(0,len(adj[u])):
            v = adj[u][i]
            if dist_values[v] == 999999:
                q.put(v)
                dist_values[v] = dist_values[u] +1
                prev_info[v] = u


    return reconstruct_path(s,t,prev_info)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
