import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    node1, node2, cost = map(int, input().split())
    graph[node1].append([cost, node2])
    graph[node2].append([cost, node1])

connected = [False]*(V+1)

def prim(graph,node):
    
    #현재 노드를 기준으로 방문하지 않은 노드를 우선순위 큐에 넣고
    #큐에서 pop 할때, 노드를 더한다. 
    connected[node] = True
    #Q는 인접노드
    Q = graph[node]
    heapq.heapify(Q)
    total_cost = 0

    while Q:
        cost, next_node = heapq.heappop(Q)    
        if not connected[next_node]:
            connected[next_node] = True
            total_cost += cost
            for i in graph[next_node]:
                if not connected[i[1]]:
                    heapq.heappush(Q,i)    
    return total_cost

print(prim(graph,1))

parent = [i for i in range(V+1)]

def find_parent(parent,idx):
    if parent[idx] != idx:
        parent[idx] = find_parent(parent,parent[idx])
    return parent[idx]
    

def union_parent(parent,A,B):
    A = find_parent(parent,A)
    B = find_parent(parent,B)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B
        
Edges = []
for _ in range(E):
    node1, node2, cost = map(int, input().split())
    heapq.heappush(Edges,[cost, node1, node2])

total_cost = 0

while Edges:
    cost, node1, node2 = heapq.heappop(Edges)
    if find_parent(parent,node1) != find_parent(parent,node2):
        union_parent(parent,node1,node2)
        total_cost += cost
print(total_cost)
