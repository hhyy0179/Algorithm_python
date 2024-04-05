import sys
input = sys.stdin.readline

N,M = map(int,input().split())

#바닥장식 - 성공
#DFS

#바닥 입력
floor = []
for _ in range(N):
    floor.append(list(input().rstrip()))

#2차원 방문 배열 초기화
visited = [[0]*M for _ in range(N)]

def dfs(x,y):
    visited[x][y] = 1
    pattern = floor[x][y]

    #패턴이 '-'이면 옆으로 이동
    if pattern == '-':
        y = y+1
    #패턴이 '|'이면 아래로 이동
    else:
        x = x+1
    if 0 <= x < N and 0 <= y < M:
        #패턴이 다르면 리턴
        if pattern == floor[x][y]:
            dfs(x,y)
        else:
            return

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1
print(cnt)
