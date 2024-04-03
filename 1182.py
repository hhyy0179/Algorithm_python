import sys
input = sys.stdin.readline

#부분수열의 합(실패)
#브루트포스, 백트래킹

#TC는 맞는데, 어떤 반례가 있는지 모르겠다 ㅠㅠ 

N, S = map(int,input().split())
numlst = list(int(x) for x in input().split())

visited = []
cnt = 0

def sumseq(num):
    global cnt,S
    #종료 조건
    if sum(visited) == S and len(visited) > 0:
        cnt += 1
    
    #중복 방지
    for i in range(num,N):
        #if numlst[i] not in visited:
        visited.append(numlst[i])
        #print(visited)
        sumseq(i+1)
        visited.pop()

sumseq(0)
print(cnt)
