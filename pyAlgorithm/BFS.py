from collections import deque

graph= [
    [],
    [2,4,7], #1번노드
    [1], #2번노드
    [2,7], #3번노드
    [5,6], #4번노드
    [3,4], #5번노드
    [4], #6번노드
    [1,3] #7번노드
]

N = len(graph)
visited = [False] * N
q = deque()

def bfs(graph,node):
    q.append(node)
    visited[node] = True

    while q:
        v = q.popleft() #4
        print(v,end = " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    

bfs(graph,1)