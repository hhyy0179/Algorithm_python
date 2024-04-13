import sys
input = sys.stdin.readline


N, M = map(int, input().split())

lst = []

def dfs():
    if len(lst) == M:
        print(' '.join(map(str,lst)))
    
    for i in range(1,N+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

dfs()





