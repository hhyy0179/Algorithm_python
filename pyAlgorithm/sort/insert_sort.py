import sys
#input = sys.stdin.readline().rstrip() # 빠른 입력
#print = sys.stdout.write # 빠른 출력

arr = [46, 34, 25, 12, 57, 93, 1, 123]
lastidx = len(arr)

for end in range(1, len(arr)):
    to_insert = arr[end]
    idx = end
    while idx > 0 and arr[idx - 1] > to_insert:
        arr[idx] = arr[idx - 1]
        idx -= 1
    arr[idx] = to_insert


