import sys
from collections import deque
input = sys.stdin.readline
#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N,M = map(int,input().split())



def bfs(miro, start_x, start_y):
    q = deque()
    q.append((start_x,start_y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < M and miro[X][Y] == 1:
                if X > 0 or Y > 0:
                    q.append((X,Y))
                    miro[X][Y] = miro[x][y] + 1
    return miro[N-1][M-1]

miro = []
for i in range(N):
    miro.append(list(map(int, input().rstrip())))
#print(miro)
print(bfs(miro,0,0))
