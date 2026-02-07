import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 0은 빈 칸, 1은 집, 2는 치킨집
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            house.append((i, j))
        elif board[i][j]==2:
            chicken.append((i, j))

ans = float('inf')
for chic in combinations(chicken, M):
    sumdis = 0
    for h in house:
        dis = 2*N
        for c in chic:
            dis = min(dis, abs(h[0]-c[0])+abs(h[1]-c[1]))
        sumdis += dis
    ans = min(ans, sumdis)
print(ans)