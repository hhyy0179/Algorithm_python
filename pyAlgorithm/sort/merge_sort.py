import sys
import random
#input = sys.stdin.readline().rstrip() # 빠른 입력


#arr1 = random.sample(range(1,100),10)

arr1 = [24, 76, 70, 94, 20, 73, 38, 43, 98, 81]   
print(arr1)

#분할 파트
def merge_sort(arr):
    if len(arr) <= 1: # 종료 조건: arr 길이가 1일때 종료
        return arr

    mid = len(arr) // 2
    # 배열 슬라이싱: 깊은 복사로 배열을 복사
    # arr[a:b] -> a ~ (b-1) 인덱스까지 복사
    print(arr[:mid], arr[mid:])
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

#정복 파트 
def merge(left, right): 
    result = []
    i = j = 0
    print("-------")
    print("merge: ",left, right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 더이상 한쪽 배열에 비교 대상이 없을 때,
    # 배열 안에 n개는 정렬이 되어있는 상태이므로 순서대로 넣어줌. 
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    print("result: ",result)
    print("-------")

    return result

sorted_arr = merge_sort(arr1)

print(sorted_arr)
    