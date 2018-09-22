#Uses python3

import sys
import queue


class dk_node():

    def __init__(self,distance,node_id):
        self.distance = distance
        self.node_id = node_id

    def __lt__(self, other):

        if self.distance < other.distance:
            return True
        else:
            return False

def distance(adj, cost, s, t):


    H = queue.PriorityQueue()

    dist = [99999 for _ in range(len(adj))]
    prev = [False for _ in range(len(adj))]

    dist[s] = 0

    for x in range(len(dist)):
        H.put(dk_node(dist[x],x))

    while H.qsize() != 0:
        current = H.get()


        for i in range(len(adj[current.node_id])):

            v = adj[current.node_id][i]

            if dist[v] > dist[current.node_id] + cost[current.node_id][i]:
                dist[v] = dist[current.node_id] + cost[current.node_id][i]
                prev[v] = current.node_id
                H.put(dk_node(dist[v],v))




    if dist[t] == 99999:
        return -1

    else:
        return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
