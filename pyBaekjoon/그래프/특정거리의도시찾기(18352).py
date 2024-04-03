import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [ [] for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)

visited = [0]*(N+1)

def bfs(graph,start):
    q = deque()
    visited[start] = 1
    q.append(start)
    cities = []

    while q:
        node = q.popleft()
        for v in graph[node]:
            if not visited[v]:
                visited[v] = visited[node] + 1
                q.append(v)
                if visited[v] == K+1:
                    cities.append(v)
    if len(cities) > 0:
        cities.sort()
        for city in cities:
            print(city)
    else:
        print(-1)
            
bfs(graph,X)
