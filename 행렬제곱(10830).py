import sys
input = sys.stdin.readline

N,B = map(int,input().split())

arr = [[ int(x) for x in input().split() ] for _ in range(N)]

#행렬 arr1와 arr2를 곱함.
def multiply(arr1,arr2):





# 행렬 A를 거듭제곱함.
def pow(A,B):
    if B == 1:
        return A
    temp = pow(A,B//2)
    if B % 2:
        return multiply(A, multiply(temp,temp))
    else:
        return multiply(temp,temp)

