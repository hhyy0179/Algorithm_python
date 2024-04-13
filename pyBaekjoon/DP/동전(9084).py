import sys
input = sys.stdin.readline

TC = int(input().rstrip())

for _ in range(TC):
    n = int(input().rstrip())
    money = list(map(int, input().split()))
    money.insert(0, 0)
    result = int(input().rstrip())

    dp = [[0]*(result+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(result+1):
            if j == 0:
                dp[i][j] = 1
            elif j < money[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-money[i]]

    print(dp[-1][-1])

    