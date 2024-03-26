import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    N, S = map(str,input().split())
    result = ""
    for s in S:
        for _ in range(int(N)):
            result += s
    print(result)
