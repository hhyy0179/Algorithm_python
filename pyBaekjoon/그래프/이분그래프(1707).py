import sys
from collections import deque
input = sys.stdin.readline

TC =int(input())

for _ in range(TC):
    V,E = map(int,input().split())
    graph = [ [] for _ in range(V+1)]
    color = ['B']* (V+1)
    visited = [False] * (V+1)
    q = deque()
    flag = False

    for e in range(E):
        n1 ,n2 = map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for i in range(1,V+1):
        if not visited[i]:
            visited[i] = True
            q.append(i)
            while q:
                node = q.popleft()
               
                for v in graph[node]:
                    if not visited[v]:
                        if color[node] == 'B':
                            color[v] = 'R'
                        visited[v] = True
                        q.append(v)
                    else:
                        if color[node] == color[v]:
                            flag = True
                            break
             
    if flag:
        print('NO')
    else:
        print('YES')
                





        

