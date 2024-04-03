import sys
input = sys.stdin.readline

#dp[1 ~ 3]
# dp = [0 for _ in range(1000000)]
# N = int(input())
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for n in range(N):
#     num = int(input())
#     for i in range(4,num+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     print(dp[num])

def Sum123(num):
    if num <= 2:
        return num
    if num == 3:
        return 4
    return Sum123(num-1) + Sum123(num-2) + Sum123(num-3)

print(Sum123(7))







