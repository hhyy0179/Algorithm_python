import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())

visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

def dfs(graph,node): 
    visited1[node] = True
    print(node, end= ' ')
    for v in graph[node]:
        if not visited1[v]:
            dfs(graph,v)

def bfs(graph,node):
    q = deque()
    visited2[node] = True
    q.append(node)

    while q:
        node = q.popleft()
        print(node, end= ' ')
        for v in graph[node]:
            
            if not visited2[v]:
                q.append(v)
                visited2[v] = True

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for arr in graph:
    arr.sort()

dfs(graph,V)
print()
bfs(graph,V)