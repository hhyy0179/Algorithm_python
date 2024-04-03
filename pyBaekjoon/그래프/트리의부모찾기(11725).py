import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
parent = {}
visited = [False]*(N+1)

def dfs(graph,node):
    visited[node] = True
    for v in graph[node]:
        if not visited[v]:
            parent[v] = node
            dfs(graph,v)

for i in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(graph,1)

sorted_graph = sorted(parent.items())
for i in sorted_graph:
    print(i[1])

