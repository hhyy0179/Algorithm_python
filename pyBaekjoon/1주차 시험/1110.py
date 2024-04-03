import sys
input = sys.stdin.readline

#더하기 사이클(성공)
#수학,구현

N = int(input())
new = N
cnt = 0
while True:
    left = new // 10
    right = new % 10

    sum_right = (left + right) % 10

    new = right*10 + sum_right
    
    cnt += 1
    if new == N:
        print(cnt)
        break
