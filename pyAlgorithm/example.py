# V : 정점의 개수, E : 간선의 개수 
V,E = map(int,input().split())

# 인접 행렬
adjArr = [[0]*(V+1) for _ in range(V+1)]

# 인접 리스트
adjList = [[] for _ in range(V+1)]

#간선 수만큼 노드 삽입
for i in range(E):
	#노드 간 연결 입력(ex. 1 2 -> 1번과 2번 사이에 간선존재)
    a, b = map(int,input().split())
    
    #양방향 그래프
    adjArr[a][b] = 1 
    adjArr[b][a] = 1 

    adjList[a].append(b)
    adjList[b].append(a)

print(adjArr)
print(adjList)