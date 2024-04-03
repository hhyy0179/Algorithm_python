import sys
input = sys.stdin.readline

num = int(input())
cnt = 1
new = num
while True:
    firstnum = new // 10 
    secondnum = new - firstnum*10

    sumnum = firstnum + secondnum
    sum_firstnum = sumnum // 10
    sum_secondnum = sumnum - sum_firstnum*10

    new = secondnum*10 + sum_secondnum

    if new == num:
        print(cnt)
        break
    else:
        cnt += 1