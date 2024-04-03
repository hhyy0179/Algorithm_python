import sys
import random

#init_arr = [76, 24, 70, 94, 20, 73, 38, 43, 98, 81]   
init_arr = [23,7,13,5,47,33,17]
print(init_arr)

def quick_sort1(arr):
    if len(arr) < 2:
        return arr;

    pivot = arr[0]
    print("pivot: ",arr[0])
    low = []
    high = []
    for value in arr[1:]:
        if value < pivot:
            low.append(value)
        else: high.append(value)
    print(f"{low} + {[pivot]} + {high}")
    return quick_sort1(low) + [pivot] + quick_sort1(high)

def quick_sort2(array, start, end):
    #start와 end가 같아지면 종료 
    if start >= end:
        return
    pivot = start #피벗 초기값은 첫번째 요소
    left = start+1
    right = end
    print("start, end: ",start, end)
    print("pivot: ",pivot, array[pivot])
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start an d array[right] >= array[pivot]:
            right-=1
        print(f"left: {array[left]} , right: {array[right]} ")
        if left>right: # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
            array[left], array[right] = array[right], array[left]
        
        print(array)
        print("============")
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort2(array, start, right-1)
    quick_sort2(array, right+1, end)
    


#sorted_arr = quick_sort1(init_arr)
sorted_arr = quick_sort2(init_arr, 0, len(init_arr)-1)


print(sorted_arr)