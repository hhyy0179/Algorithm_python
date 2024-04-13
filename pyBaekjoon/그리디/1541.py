

prob = input().split('-')
ans = 0
for i in range(len(prob)):
    num = 0
    plusnum = prob[i].split('+')
    for n in plusnum:
        num += int(n)
        
    if i > 0:
        ans -= num
    else:
        ans += num

print(ans)