import sys
from collections import deque
input = sys.stdin.readline

#단지번호 붙이기 - 성공
#BFS

#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input().rstrip())

#배열 입력
graph = []
for _ in range(N):
    graph.append(list(map(int,input().rstrip())))
#print(graph)

def bfs(x,y):
    q = deque()

    #큐에 담으면 0으로 방문처리
    q.append((x,y))
    graph[x][y] = 0
    #방문 개수
    cnt = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < N:
                #방문 안했으면, 큐에 담고 방문처리
                if graph[X][Y] == 1:
                    q.append((X,Y))
                    graph[X][Y] = 0
                    #방문처리 하면, 개수 + 1 
                    cnt += 1
    return cnt

total_cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            total_cnt.append(bfs(i,j))

#정렬 후, 출력
total_cnt.sort()

print(len(total_cnt))
for cnt in total_cnt:
    print(cnt)
