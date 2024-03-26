import sys
input = sys.stdin.readline().rstrip()

num = int(input)

for i in range(1,10):
    print(f"{num} * {i} = {num*i}")