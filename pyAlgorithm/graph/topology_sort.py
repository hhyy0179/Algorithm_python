from collections import deque,defaultdict

graph = [
    [],
    [2,4], #1번 노드와 연결
    [3], #2번 노드와 연결
    [4], #3번 노드와 연결
    [5], #4번 노드와 연결
    [], #5번 노드와 연결
]

N = len(graph)
q = deque()
indegree = defaultdict(int)


for i in range(1,N):
   for j in graph[i]:
      indegree[j] += 1 

def topology_sort(graph):
    for node in range(1,len(graph)):
        if not indegree[node]:
            q.append(node)
            
    while q:
        next_node = q.popleft()
        print(next_node,end= " ")
        for v in graph[next_node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

topology_sort(graph)


