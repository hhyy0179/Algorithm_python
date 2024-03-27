import sys
input = sys.stdin.readline

blue = white = 0

def cutPaper(arr):
    n = len(arr[0])
    color = arr[0][0]
    is_recur = False
    global blue,white

    for i in range(n):
        for j in range(n):
            if arr[i][j] != color:
                is_recur = True
                break
    if is_recur:
        #이렇게 하면 2차원 배열 slicing 안됨.
        # cutPaper(arr[:mid][:mid])
        # cutPaper(arr[:mid][mid:])
        # cutPaper(arr[mid:][:mid])
        # cutPaper(arr[mid:][mid:])
        mid = n // 2

        #이렇게 해야 2차원 배열 slicing 가능
        cutPaper(list(arr[m][:mid] for m in range(mid)))
        #print(list(arr[m][mid:] for m in range(mid)))
        cutPaper(list(arr[m][mid:] for m in range(mid)))
        cutPaper(list(arr[m][:mid] for m in range(mid,len(arr))))
        cutPaper(list(arr[m][mid:] for m in range(mid,len(arr))))
    else:
        if color == 1:
            blue += 1
        else:
            white += 1
        return

N = int(input())
arr = [[int(x) for x in input().split()] for y in range(N)]
cutPaper(arr)
print(white)
print(blue)
