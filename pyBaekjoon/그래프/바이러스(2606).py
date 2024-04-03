import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

parent = [ i for i in range(V+1)]

def find_parent(parent,idx):
    if idx != parent[idx]:
        parent[idx] = find_parent(parent,parent[idx])
    return parent[idx]



for e in range(E):
    n1, n2 = map(int,input().split())
    n1_p = find_parent(parent,n1)
    n2_p = find_parent(parent,n2)
    if n1_p != n2_p:
        parent[max(n1_p,n2_p)] = min(n1_p,n2_p)
for i in range(V+1):
    find_parent(parent,i)

print(parent.count(1)-1)