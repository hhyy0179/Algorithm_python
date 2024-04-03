import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(graph,start,end):
    q = [(0, start)]
    distance = defaultdict(int)

    while q:
        cost, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = cost
            if node == end:
                return cost
            for v, w in graph[node]:
                update = cost + w
                heapq.heappush(q,(update,v))
    return

N = int(input().rstrip())
M = int(input().rstrip())
graph = defaultdict(list) # 빈 그래프 생성
for _ in range(M):
    start,end,cost = map(int, input().split())
    graph[start].append((end,cost))

start_point, end_point = map(int,input().split())
print(dijkstra(graph,start_point,end_point))