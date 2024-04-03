import sys
#input = sys.stdin.readline().rstrip() # 빠른 입력
#print = sys.stdout.write # 빠른 출력

arr = [64, 34, 25, 12, 57, 93, 1, 123]
last = len(arr)


print(arr)
for idx in range(last-1):
    minidx = idx
    for find in range(idx+1,last):
        if arr[find] < arr[minidx]:
            minidx = find
    arr[idx],arr[minidx] = arr[minidx],arr[idx]

print(arr)
    
        