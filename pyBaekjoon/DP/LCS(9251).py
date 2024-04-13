import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
N = len(str1)+1
M = len(str2)+1


LCS = [[0]*M for _ in range(N)]

for i in range(1,N):
    for j in range(1,M):
        
        #문자열이 같을 경우
        if str1[i-1] == str2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
    
        #문자열이 다를 경우
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(LCS[-1][-1])

