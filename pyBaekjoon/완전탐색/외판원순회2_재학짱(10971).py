import sys

N = int(input().rstrip())
graph = []
for _ in range(N):
    arr = list(map(int, input().rstrip().split()))
    graph.append(arr)

mincnt = sys.maxsize

def dfs(start, cnt, visited):
    global mincnt
    if len(visited) == N:
        st = visited[0]
        en = visited[-1]
        if graph[en][st]:
            cnt += graph[en][st]
            mincnt = min(mincnt, cnt)
        return

    for i in range(N):
        if i not in visited and graph[start][i]:
            visited.append(i)
            cnt += graph[start][i]
            dfs(i, cnt, visited)
            cnt -= graph[start][i]
            visited.pop()


dfs(0, 0, [0])  
print(mincnt)
