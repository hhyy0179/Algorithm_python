import sys
input = sys.stdin.readline
#쿼드트리(성공)
#분할정복, 재귀

N = int(input())


#img = [list(x) for x in input().rstrip()]

#배열 입력
img = []
for i in range(N):
    row = input().rstrip()
    img.append(list(row))
#print(img)

ans = ''
def quartree(arr):
    global ans
    n = len(arr[0])
    color = arr[0][0]
    recur = False
    for i in range(n):
        for j in range(n):
            if arr[i][j] != color:
                recur = True
                break
    if recur:
        mid = n // 2
        #2차원 배열 slicing 가능
        ans += '('
        quartree(list(arr[m][:mid] for m in range(mid)))
        quartree(list(arr[m][mid:] for m in range(mid)))
        quartree(list(arr[m][:mid] for m in range(mid,len(arr))))
        quartree(list(arr[m][mid:] for m in range(mid,len(arr))))
        ans += ')'
    else:
        if color == '1':
            ans += '1'
        else:
            ans += '0'

quartree(img)
print(ans)