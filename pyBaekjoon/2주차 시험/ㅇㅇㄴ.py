import sys

n , m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(sys.stdin.readline().strip())

count = 0
for i in range(n):
    result = graph[i].split("|")
    #print(result)
    for j in result:
        if j != "":
            count +=1


for i in range(m):
    new = []
    for j in range(n):
        new+=graph[j][i]
       
        new1 = ""
    print(new)
    for k in range(len(new)):
        new1+=new[k]
    result = new1.split("-")
    print(result)
    for h in result:
        if h !="":
            count+=1
print(count) 