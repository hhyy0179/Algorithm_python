import sys
input = sys.stdin.readline

tile = [1,2]

N = int(input().rstrip())

for i in range(2,N):
    new_tile = (tile[i-1] + tile[i-2]) % 15746
    tile.append(new_tile) 

print(tile[N-1])



