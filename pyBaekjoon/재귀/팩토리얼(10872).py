import sys
input = sys.stdin.readline().rstrip()

N = int(input)

def Factorial(n):
    if n <= 1:
        return 1
    return n*Factorial(n-1)

print(Factorial(N))