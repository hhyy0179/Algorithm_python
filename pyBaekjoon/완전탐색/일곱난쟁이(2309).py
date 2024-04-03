import sys
from itertools import combinations
input = sys.stdin.readline
heights = []
for i in range(9):
    height = int(input())
    heights.append(height)

comb = list(combinations(heights,7))

print()
for c in comb:
   if sum(c) == 100:
        for j in sorted(c):
            print(j)
        break
