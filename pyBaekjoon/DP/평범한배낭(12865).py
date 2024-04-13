import sys
input = sys.stdin.readline

#아이템 수, 가방 최대 무게
N,K = map(int,input().split())

itemlist = [[0,0]]
for _ in range(N):
    weight, value = map(int, input().split())
    itemlist.append([weight,value])

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w, v = itemlist[i][0], itemlist[i][1]

    for j in range(1,K+1):
        if j < w :
            dp[i][j] = dp[i-1][j]
        else:
            #현재 물건은 (이전 상황에서 최대 value + 현재 무게 value)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])


