import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
#deque 는 각 명령을 O(1)으로 지원하는데에 반해,
#Queue 모듈은 멀티쓰레드 환경을 지원하기 때문에 더 느리다고 함....

for i in range(N):
   
    #아래 명령은 굳이 쓰지 말자
    #cmdline = list(map(str,input().split()))

    #굳이 배열 길이 비교하는 것도 하지 말ㅈ ㅏ...

    
    cmdline = input().split()
    cmd = cmdline[0]

    if cmd == "push":
        queue.append(cmdline[1])

    if cmd == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
        
    if cmd == "size":
        print(len(queue))

    if cmd == "empty":
        if len(queue):
            print(0)
        else: print(1)

    if cmd == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)

    if cmd == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)



