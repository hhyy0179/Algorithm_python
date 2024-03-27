import sys
input = sys.stdin.readline

N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

def binary_search(arr,target):
    start = 0;
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0
num1.sort()
for n in num2:
    print(binary_search(num1,n))


