
graph = [
    [], 
    [2,3,5,6], #1번노드
    [1,4,7], #2번노드
    [1,6], #3번노드
    [2], #4번노드
    [1], #5번노드
    [1,3,7], #6번노드
    [2,6,8], #7번노드
    [7] #8번노드
]

N = len(graph) #9
visited = [False] * N

def dfs(graph,node):
    visited[node] = True
    print(node, end = " ")
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i)

dfs(graph,1)