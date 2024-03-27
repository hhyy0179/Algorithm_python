N = int(input())

#에라토스테네스의 체

n = 10000
primes = []
a = [False,False] + [True]*(n-1)
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for _ in range(N):
    num = int(input())
    num1 = num2 = num//2
    
    while True:
        if (num1 in primes) and (num2 in primes):
            print(num1, num2)
            break
        else:
            num1 -= 1
            num2 += 1
    
            


