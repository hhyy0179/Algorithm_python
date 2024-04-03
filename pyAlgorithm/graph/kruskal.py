
# 1. 간선 비용이 낮은 순으로 정렬
# 2. 현재 추가할 간선이 사이클을 발생시키는 지 확인
# 3. 사이클 발생 안하는 경우 -> mst에 포함.
# 4. 사이클 발생하는 경우 -> mst애 포함 안함.
# 5. 2~4 반복 수행


V,E = map(int,input().split())

#부모 테이블 초기화
parent = [i for i in range(0,V+1)]

#부모 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#다른 그룹이면, 병합(부모 업데이트)
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
#a= 2 b = 7
    
    #부모의 부모 값으로 변경*******
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0

for _ in range(E):
    start, end, cost = map(int, input().split())
    edges.append((cost,start,end))

edges.sort()

for i in range(E):
    cost, start, end = edges[i]
    
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent,start,end)
        print("=====")
        print(f'{start} -> {end} : {cost} / parent[{parent[start]}]')
        total_cost += cost 
    else:
        print(f'{start} -> {end} : make cycle!')

print(total_cost)
print(parent)

