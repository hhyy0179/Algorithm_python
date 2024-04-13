import sys
import heapq
input = sys.stdin.readline

#신입 사원
#그리디
#서류심사 성적과 면접심사 성적 중, 
#적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발. 
#신입사원의 최대 인원수를 구해야함, 

TC = int(input().rstrip())

for _ in range(TC):
    N = int(input().rstrip())
    grade = []
    cnt = 0
    for n in range(N):
        first, second = map(int, input().split())
        heapq.heappush(grade,(first,second))
    max_first, max_second = N,N
    while grade:
        first, second = heapq.heappop(grade)
        if first <= max_first or second <= max_second:
            max_first = first
            max_second = second
            cnt += 1
    print(cnt)

