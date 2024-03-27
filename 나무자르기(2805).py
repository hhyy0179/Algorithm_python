import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

#자르려는 높이 탐색
while start <= end:
    mid = (start + end) // 2
    #가져가려고 하는 나무 길이
    get = 0
    for t in trees:
        if t > mid: #자르려는 높이보다 크면
            get += (t - mid)
            
    #적어도 M이므로 get이 무조건 M이 나오진 않는다... 
    # if get == M:
    #     print(mid)
    #     break
            
    #얻은 양이 많으면 높이를 키우자
    if get >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

  


