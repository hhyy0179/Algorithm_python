import sys
from collections import defaultdict
input = sys.stdin.readline


N = int(input().rstrip())

graph = {}
for i in range(N):
    node, left, right = map(str, input().split())
    graph[node] = [left,right]

def pre_order_traverse(node):
    if node == '.':
        return
    print(node,end ='')
    pre_order_traverse(graph[node][0])
    pre_order_traverse(graph[node][1])

def in_order_traverse(node):
    if node == '.':
        return
    
    in_order_traverse(graph[node][0])
    print(node,end ='')
    in_order_traverse(graph[node][1])


def post_order_traverse(node):
    if node == '.':
        return
    post_order_traverse(graph[node][0])
    post_order_traverse(graph[node][1])
    print(node,end ='')


pre_order_traverse('A')
print()
in_order_traverse('A')
print()
post_order_traverse('A')
