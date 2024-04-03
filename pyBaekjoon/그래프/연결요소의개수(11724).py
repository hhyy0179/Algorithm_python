import sys
input = sys.stdin.readline

N,M = map(int,input().split())

parent = [i for i in range(N+1)]

def find_parent(parent,idx):
    if idx != parent[idx]:
        parent[idx] = find_parent(parent,parent[idx])
    return parent[idx]

def union_parent(parent,A,B):
    A = find_parent(parent,A)
    B = find_parent(parent,B)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

for _ in range(M):
    node1, node2 = map(int, input().split())
    if find_parent(parent,node1) != find_parent(parent,node2):
        union_parent(parent,node1,node2)
for idx in range(1,N+1):
    find_parent(parent,idx)

print(len(set(parent))-1)

