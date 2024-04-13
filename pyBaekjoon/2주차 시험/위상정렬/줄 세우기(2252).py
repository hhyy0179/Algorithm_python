import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

def sort_line(graph,indegree):
    q = deque()
    #진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, len(indegree)):
        if not indegree[i]:
            q.append(i)

    while q:
        node = q.popleft()
        print(node,end = ' ')
        for v in graph[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

for _ in range(M):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    indegree[n2] += 1

sort_line(graph,indegree)
