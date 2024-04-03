import sys
from collections import deque
input = sys.stdin.readline

#deque는 double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조 이다.
# list에는 없는 popleft()라는 메서드를 제공한다.

N, M = map(int,input().split())
numlist = deque()
ans = "<"

for i in range(1,N+1):
    numlist.append(i)

while len(numlist):
    for _ in range(M-1):
        numlist.append(numlist.popleft())
    if len(numlist) == 1:
        ans += str(numlist.popleft()) + ">"
    else:
        ans += str(numlist.popleft()) + ", "

print(ans)
