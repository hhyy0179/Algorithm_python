import sys
input = sys.stdin.readline

N, K = map(int,input().split())

money = []
for _ in range(N):
    money.append(int(input().rstrip()))
money.reverse()

ans = 0
for m in money:
    ans += K // m
    #거스름돈
    K = K % m 
print(ans)
        
        
        
