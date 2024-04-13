import sys
input = sys.stdin.readline

N = int(input().rstrip())

matrixs = []
for _ in range(N):
    matrix = list(map(int,input().split()))
    matrixs.append(matrix)


dp = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0

#3~1
k = 0
for i in range(N-1,-1,-1):
    k += 1
    for j in range(i):
        cnt += 1
        dp[j][j+k] = cnt

for a in dp:
    print(a)