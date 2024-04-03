import sys
from collections import defaultdict
input = sys.stdin.readline
graph = [0] * 40000
maxidx = 0
while True:
    try: 
        node = int(input().rstrip())
        idx = 0
        while True:
            #작으면, 왼쪽 노드 삽입
            if node < graph[idx]:
                idx = idx * 2
            #크면, 오른쪽 노드 삽입
            else:
                idx = (idx * 2) + 1
            if graph[idx] == 0:
                graph[idx] = node
                maxidx = max(maxidx,idx)
                break  
    except:
        break

graphlist = {}

for i in range(1,maxidx+1):
    if graph[i]:
        graphlist[graph[i]] = [graph[i*2],graph[(i*2)+1]]

def post_order_traverse(node):
    if node == 0 :
        return
    post_order_traverse(graphlist[node][0])
    post_order_traverse(graphlist[node][1])
    print(node)

post_order_traverse(graph[1])

