import sys
input = sys.stdin.readline

#계단오르기 - 성공~

N = int(input().rstrip())

#입력 배열 만들기
stair = [0]*(N+3)
for s in range(1,N+1):
    stair[s] = int(input())


#dp 배열 - 해당 위치까지 갔을 때,얻을 수 있는 최대 value값
dp = [0]*(N+3)

#초기값 선언
dp[1] = stair[1] 
dp[2] = stair[1]+stair[2] #두개 다 밟아야 이득

for i in range(3,N+3):
    #전전 칸을 밟는 경우 vs 바로 전칸 밟는 경우(그 경우 전전전칸을 밟은 상태여야함.)
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

print(dp[N])