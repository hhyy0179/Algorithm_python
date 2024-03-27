import sys

input = sys.stdin.readline

N = int(input())

#파이썬은 list가 스택이다..
stk = []
for i in range(N):
    cmdline = list(map(str,input().split()))

    if len(cmdline) > 1:
        data = int(cmdline[1])
    cmd = cmdline[0]

    if cmd == "push":
        stk.append(data)
    if cmd == "pop":
        if len(stk):
            print(stk[-1])
            stk.pop()
        else:
            print(-1)
    if cmd == "size":
        print(len(stk))
    if cmd == "empty":
        if len(stk):
            print(0)
        else:
            print(1)
    if cmd == "top":
        if not len(stk):
            print(-1)
        else:
            print(stk[-1])


