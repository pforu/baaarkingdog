import sys
input = sys.stdin.readline
from itertools import combinations

N, M, H = map(int, input().split())
lad = [[0]*(N+1) for _ in range(H+1)]
able = set()
for i in range(1, H+1):
    for j in range(1, N):
        able.add((i, j))
for _ in range(M):
    a, b = map(int, input().split())
    lad[a][b], lad[a][b+1] = b+1, b
    able.remove((a, b))

ans = -1
stop = False
for i in range(0, 4):
    if stop: break
    for c in combinations(able, i):
        if stop: break
        
        impos = False
        for a, b in c:
            if lad[a][b]!=0 or lad[a][b+1]!=0: # 연속하지 않게 주의 
                impos = True
                break
        if impos:
            continue

        for a, b in c:
            lad[a][b], lad[a][b+1] = b+1, b
        
        find = True
        for ver in range(1, N+1):
            pos = ver
            for hor in range(1, H+1):
                to = lad[hor][pos]
                if to!=0:
                    pos = to
            if pos!=ver:
                find = False
                break
        if find:
            ans = i
            stop = True
            break

        for a, b in c:
            lad[a][b], lad[a][b+1] = 0, 0

print(ans)
