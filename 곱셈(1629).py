import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

# 처음에 return 자체에 재귀호출을 했는데. 그렇게 하면 O(logN)이 아니라 
# O((logN)^2)이 되므로 계속해서 시간초과가 났다...ㅎ
# 당연한건데 오답 코드로 4번이나 제출했음 .. 함수 호출 횟수에 유의하쟈! ㅎ
# 모듈러 연산: (A * B) % C = (A%C * B%C) % C
# 모듈러 연산은 + - * 에 대해서 모두 적용 가능


def pow(A,B,C):
    if B == 0:
        return 1
    
    Divide = pow(A,B//2,C)

    #B가 홀수이면
    if B % 2:
       return Divide * Divide * A % C
    #B가 짝수이면
    else:
        return Divide * Divide % C

print(pow(A,B,C))