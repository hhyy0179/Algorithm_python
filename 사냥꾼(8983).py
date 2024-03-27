import sys
input = sys.stdin.readline

M,N,X = map(int,input().split())

hunt = list(map(int,input().split()))

hunt.sort()

def binary_search(arr, target_x, target_y):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if target_x >= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(arr):
        dist = (target_x - arr[end]) + target_y
    elif end < 0:
        dist = (arr[start] - target_x) + target_y
    else:
        dist = min(arr[start] - target_x, target_x - arr[end]) + target_y
    return dist

cnt = 0
for i in range(N):
    x, y = map(int,input().split())
    if binary_search(hunt,x,y) <= X:
        cnt += 1

print(cnt)


