import sys
input = sys.stdin.readline

N = int(input())

#https://velog.io/@shin75492/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B0%EC%97%B4-%EC%9E%85%EB%A0%A5-%EB%B0%9B%EA%B8%B0-%EC%A0%95%EB%A6%AC
#파이썬 입력 여러 방식

arr = [[int(x) for x in input().split()] for y in range(N)]
lst = [0]
mincnt = 1e9

def dfs(start,cnt):
    global mincnt
    if len(lst) == N:
        st = lst[0]
        ed = lst[-1]
        if arr[ed][st]:
            cnt += arr[ed][st]
            mincnt = min(mincnt,cnt)
        return 
    
    #1~4까지
    for i in range(N):
        if i not in lst and arr[start][i]:
            lst.append(i)
            cnt += arr[start][i]
            if cnt < mincnt:
                dfs(i,cnt)
            cnt -= arr[start][i]
            lst.pop()

dfs(0,0)
print(mincnt)


