import heapq
from collections import defaultdict

V,E = map(int,input().split())
connected = [False]*(V+1)

graph = [[] for _ in range(V+1)]
mst = []

for i in range(E):
    start, end, weight = map(int,input().split())
    graph[start].append([weight,end])
    graph[end].append([weight,start])

print(graph)

def prim(graph,node):
    connected[node] = True
    candidate = graph[node]
    heapq.heapify(candidate)

    total_weight = 0
    while candidate:
        weight, next_node = heapq.heappop(candidate)    
        if not connected[next_node]:
            connected[next_node] = True
            total_weight += weight

            for v in graph[next_node]: 
                if not connected[v[1]]:
                    heapq.heappush(candidate,v)

    return total_weight

prim(graph,1)

# 7 9
# 1 2 5
# 1 3 2
# 2 3 6
# 3 4 7
# 2 5 3
# 4 5 1
# 2 6 2
# 5 7 4
# 6 7 5
