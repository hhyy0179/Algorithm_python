from collections import deque

graph = [
    [],
    [3,4,5,6], #1번 노드와 연결
    [3,4], #2번 노드와 연결
    [1,2,6,7,9], #3번 노드와 연결
    [1,2,7,8], #4번 노드와 연결
    [1,7,8], #5번 노드와 연결
    [1,3], #6번 노드와 연결 
    [3,5,7,9], #7번 노드와 연결
    [4,5,7], #8번 노드와 연결
    [3,7] #9번 노드와 연결
]
N = len(graph)
q = deque()
visited = [False]*N

def bfs(graph,node):
    visited[node] = True
    q.append(node)
    while q:
        next_node = q.popleft()
        for v in graph[next_node]:
            if not visited[v]:
                q.append(v)
                visited[v] = True

bfs(graph,1)


