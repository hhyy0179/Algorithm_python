n = int(input())
numbers = map(int, input().split())
cnt = 0

def find_prime(n):
    flag = True
    for div in range(2,n):
        if (n % div == 0):
            flag = False
    return flag

for n in numbers:
    


