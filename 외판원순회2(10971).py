import sys
input = sys.stdin.readline

N = int(input())

#https://velog.io/@shin75492/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B0%EC%97%B4-%EC%9E%85%EB%A0%A5-%EB%B0%9B%EA%B8%B0-%EC%A0%95%EB%A6%AC
#파이썬 입력 여러 방식

arr = [[int(x) for x in input().split()] for y in range(N)]
visited = [0 for i in range(N)]

def dfs(start,now,cnt,k):
    if k == N-1:
        print(now)
        return

    for i in range(N):
        cost = arr[now][i]
        print(f"arr[{now}][{i}] cost: {cost}")
        if cost and not visited[i]:
            visited[i] = True
            print(visited)
            print(f"함수 호출!: dfs({start},{i},{cnt+cost},{k+1})")
            dfs(start,i,cnt+cost,k+1)
            visited[i] = False

visited[1] = True
dfs(1,1,0,0)


