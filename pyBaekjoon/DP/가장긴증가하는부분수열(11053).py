import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int,input().split()))

dp = [1]* N

for n in range(N):
    cur = numbers[n]
    for i in range(n):
        #앞에 있는 애보다 값이 작고, 현재 dp 값보다 크거나 같으면, dp 값 + 1 
        if numbers[i] < cur and dp[n] <= dp[i]:
            dp[n] = dp[i]+1
print(max(dp))


            

