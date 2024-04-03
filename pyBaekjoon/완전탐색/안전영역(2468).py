import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

def findSafe(arr,start_x,start_y,h):

    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if (0 <= X < N) and (0 <= Y < N):
                if visited[X][Y] == False and arr[X][Y] > h:
                    visited[X][Y] = True
                    q.append((X,Y))
    


arr = [[int(x) for x in input().split()] for y in range(N)]

maxcnt = 0
for height in range(101):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visited[i][j] == False:
                findSafe(arr,i,j,height)
                cnt += 1

    if cnt > maxcnt:
        maxcnt = cnt 

print(maxcnt)

#처음에 height가 1인 상황부터 고려했지만,
# 비가 아예 오지 않을 경우까지 고려해야한다. (height가 0일 경우)
# 오랜만에 보는 bfs 였지만, 생각보다 바로바로 생각났다.. 실력이 늘었다는게 느껴져서 뿌듯했음!

