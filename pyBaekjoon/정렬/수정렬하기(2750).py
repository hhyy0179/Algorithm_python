import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

sorted_list = num_list.sort()

for n in num_list:
    print(n)
