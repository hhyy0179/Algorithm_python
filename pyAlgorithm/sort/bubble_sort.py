import sys
#input = sys.stdin.readline().rstrip() # 빠른 입력
#print = sys.stdout.write # 빠른 출력

arr = [64, 34, 25, 12, 57, 93, 1, 123]

last = len(arr)

while last > 1:
    for idx in range(last-1):
        if arr[idx] > arr[idx+1]:
            arr[idx],arr[idx+1] = arr[idx+1],arr[idx] #Swap index
    last -= 1


print(arr)



