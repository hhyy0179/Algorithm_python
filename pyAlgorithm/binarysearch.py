import sys

arr = [20, 24, 38, 43, 70, 73, 76, 81, 94, 98]

#iterative 
def binarysearch_iter(target):
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return     

#recursive
def binarysearch_recur(target,start,end):
    if start <= end :
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarysearch_recur(target,mid+1,end)
        else:
            return binarysearch_recur(target,start,mid-1)
    else:
        return
#print(binarysearch_iter(81))
print(binarysearch_recur(81,0,len(arr)-1))