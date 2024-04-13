import sys
from collections import deque
input = sys.stdin.readline

#점프 - 답은 나옴.. (메모리 초과) 
N = int(input().rstrip())

#입력 배열 만들기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

#dp 배열 0으로 초기화
dp = [[0]*N for _ in range(N)]

#큐에 시작지점 넣기
q = deque()
q.append((0,0,graph[0][0]))

while q:
    x, y, jump = q.popleft()
    #x로 jump만큼 이동
    if (x+jump) <= N-1:
        #해당 지점에 +1 
        dp[x+jump][y] += 1
        #도착 지점이 아니라면 큐에 넣기
        if not (x+jump == N-1 and y == N-1):
            q.append((x+jump,y,graph[x+jump][y]))

    #y로 jump만큼 이동
    if (y+jump) <= N-1:
        #해당 지점에 +1 
        dp[x][y+jump] += 1
        #도착 지점이 아니라면 큐에 넣기
        if not (x == N-1 and y+jump == N-1):
            q.append((x,y+jump,graph[x][y+jump]))
    
    
print(dp[-1][-1])
    
