import sys
input = sys.stdin.readline

N,S = map(int, input().split())
visited = [0] * (N+1)
cnt = 0
arr = [x for _ in input().split()]
num

def back_tracking(start):
    global cnt
    #종료 조건
    if sum == S:
        cnt += 1
        return

    for i in range(start,N):
        if visited[i] == 0 :
            visited[i] = 1
            back_tracking(i+1)
            visited[i] = 0

back_tracking(arr,0)
print()
