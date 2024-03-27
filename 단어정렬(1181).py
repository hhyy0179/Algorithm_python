import sys
input = sys.stdin.readline

num = int(input().strip())
words = dict()
for _ in range(num):
    word = input().strip()
    words[word] = len(word)

#https://jeongmin-lee.tistory.com/82
#딕셔너리 다중 조건으로 정렬하기

words = sorted(words.items(), key= lambda x : (x[1], x[0]))

for key in words:
    print(key[0])