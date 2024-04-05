import sys
import heapq
input = sys.stdin.readline

#경쟁적 전염 - 성공
#BFS

#     상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())

#배열 입력
virus = []
for _ in range(N):
    virus.append(list(map(int,input().split())))

S, X, Y = map(int, input().split())

#번호가 낮은 순으로 우선순위 큐에 담음
occupied = []
for i in range(N):
    for j in range(N):
        num = virus[i][j]
        if num:
            heapq.heappush(occupied,(num,i,j))

def bfs(occupied):
    q = []
    while occupied:
        num, x, y = heapq.heappop(occupied)

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if 0 <= X < N and 0 <= Y < N:
                #방문한 적 없으면, 방문 처리
                if not virus[X][Y]:
                    virus[X][Y] = num
                    #새로운 큐에 담음
                    heapq.heappush(q,(num,X,Y))
    return q

#시간
for t in range(S):
    occupied = bfs(occupied)
print(virus[X-1][Y-1])
        
        
