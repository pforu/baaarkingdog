import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
skill = [list(map(int, input().split())) for _ in range(N)]

ans = 3000
for c in combinations(range(N), N//2):
    start, link = 0, 0
    for p in combinations(c, 2):
        x, y = p
        start += (skill[x][y] + skill[y][x])

    others = set(range(N)) - set(c)
    for p in combinations(others, 2):
        x, y = p
        link += (skill[x][y] + skill[y][x])
    
    ans = min(ans, abs(start-link))
print(ans)
