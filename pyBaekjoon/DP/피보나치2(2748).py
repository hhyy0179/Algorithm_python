import sys
input = sys.stdin.readline

N = int(input())

Fib = [0,1]

for i in range(2,N+1):
    Fib.append(Fib[i-1] + Fib[i-2])

print(Fib[N])
