import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

total_cost = 0
def dfs(graph,start,cost,N):
    global total_cost
    if start == N:
        total_cost += cost
        return
    for v, c in graph[start]:
        dfs(graph, v, c*cost, N)

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    end, start, cnt = map(int,input().split())
    graph[start].append((end,cnt))
    indegree[end] += 1

for i in range(1,N):
    if indegree[i] == 0:
        total_cost = 0
        dfs(graph,i,1,N)
        print(i, total_cost)
