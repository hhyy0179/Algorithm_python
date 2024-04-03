#힙: 완전이진트리를 기반으로 한 자료구조

#최대 힙: 부모 노드 값이 자식 노드보다 큰 관계
#최소 힙: 자식 노드 값이 부모 노드보다 큰 관계

# 우선순위 큐: 들어오는 순서와 관계없이, 우선순위가 높은 자료가 먼저 나가는 자료구조
# 우선순위 큐를 연결리스트와 배열로 구현하지 않는 이유: 
# 우선순위대로 정렬하여 삽입/삭제가 일어날 시, 
# 배열은 최악의 경우 모든 값들을 뒤로 한 칸씩 미뤄야하므로 최악의 경우 O(n) 이고,
# 연결리스트의 경우도, 삽입/삭제는 간단하지만 수행할 위치로 이동하기 위해서는
# 최악의 경우 O(n)의 시간이 걸린다. 
# 그에 반해, 완전 이진 트리로 구현할 시, 삽입/삭제 위치는 부모와 자식간 노드만 확인하면 되기 때문에
# O(logn)의 시간복잡도를 가진다.

# heappush 구현과정
# 1. 배열 맨 끝에 값을 추가한다.
# 2. 추가한 원소의 인덱스를 구한다.
# 3. 부모 인덱스를 구하여 값을 비교한다.
# 4. 새 값이 부모 값보다 작으면(크면) 교환한다. 
# 5. 3~4번 반복
# 6. 새 값이 부모 값보다 크(작)거나 같으면 종료한다.

# heappop 구현과정
# 1. 루트 노드 값을 임시 저장한다.
# 2. 가장 마지막 인덱스 값을 루트노드에 옮긴 후, 
# 3. 자식 인덱스와 값을 비교하며
# 4. 현재 값이 자식 값보다 작으면(크면) 교환한다. 
# 5. 3~4번 반복
# 6. 새 값이 자식 값보다 크(작)거나 같으면 종료한다.

import heapq
h1 = []
h2 = []

def heappush(heap,data,priority):
    heap.append(data)
    idx = len(heap)-1 #마지막에 삽입한 데이터 인덱스

    if priority == 'max':
        #root index가 아닐 때까지
        while idx > 0:
            parent_idx = (idx - 1)//2
            if heap[parent_idx] < heap[idx]:
                heap[parent_idx],heap[idx] = heap[idx],heap[parent_idx]
                idx = parent_idx
            else:
                break
    else:
        #root index가 아닐 때까지
        while idx > 0:
            parent_idx = (idx - 1)//2
            if heap[parent_idx] > heap[idx]:
                heap[parent_idx],heap[idx] = heap[idx],heap[parent_idx]
                idx = parent_idx
            else:
                break

def heappop(heap,priority):
    
    if len(heap) == 0:
        print("Empty Heap!")
        return  
    
    pop_data, heap[0] = heap[0], heap.pop()
    idx, next_idx = 0, 1

    if priority == 'max':
        while next_idx < len(heap):
            sibling = next_idx + 1
            #오른쪽 노드가 더 큰 값이면, 큰 값으로 이동
            if sibling < len(heap) and heap[next_idx] < heap[sibling]:
                    next_idx = sibling
            if heap[next_idx] > heap[idx]:
                heap[next_idx],heap[idx] = heap[idx],heap[next_idx]
                idx = next_idx
                next_idx = idx*2 + 1
            else:
                break
    else:
        while next_idx < len(heap):
            sibling = next_idx + 1
            #오른쪽 노드가 더 작은 값이면, 작은 값으로 이동
            if sibling < len(heap) and heap[next_idx] > heap[sibling]:
                    next_idx = sibling
            if heap[next_idx] < heap[idx]:
                heap[next_idx],heap[idx] = heap[idx],heap[next_idx]
                idx = next_idx
                next_idx = idx*2 + 1
            else:
                break
        
    return pop_data       

    
                    
example =[2,8,5,7,3,4,6]

for x in example:
    heappush(h1,x,'max')
print(h1)
print('=========')
heappop(h1,'max')
print(h1)
heappop(h1,'max')
print(h1)

# for x in example:
#     heappush(h2,x,'min')
#     print(h2)