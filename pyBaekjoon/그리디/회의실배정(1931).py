import sys
import heapq
input = sys.stdin.readline

#문제: 1개의 회의실에 대해 N개의 회의실 사용표 만들기
#회의의 최대 개수 찾기
#시작시간 끝시간
#그리디 알고리즘:

N = int(input().rstrip())

timelst = []
for _ in range(N):
    start, end = map(int,input().split())
    heapq.heappush(timelst,(end,start))

cnt, cur_end, cur_start = 0 ,0, 0
while(timelst):
    #끝나는 시간 시작 시간
    end, start = heapq.heappop(timelst)
    
    #시작시간이 끝나는 시간보다 크다면,
    if start >= cur_end:
        cur_end = end
        cur_start = start
        cnt += 1
    else:
        continue

print(cnt)