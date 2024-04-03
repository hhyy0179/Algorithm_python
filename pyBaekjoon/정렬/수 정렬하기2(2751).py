import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
arr.sort()
for n in arr:
    print(n)

