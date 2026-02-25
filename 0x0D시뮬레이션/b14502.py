import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

vis_raw = [[False]*M for _ in range(N)]
blank = []
cnt0 = -3 # 벽 3개 세웠을 때 빈칸 개수 

virpos = []
for i in range(N):
    for j in range(M):
        val = board[i][j]
        if val==2:
            vis_raw[i][j] = True
            virpos.append((i, j))
        elif val==0:
            blank.append((i, j))
            cnt0 += 1

safe = 0 # 최대 빈칸 개수 
for c in combinations(blank, 3):
    nvirus = cnt0 # 안전지대 

    vis = [row[:] for row in vis_raw]
    Q = deque()

    for b in c:
        vis[b[0]][b[1]] = True # 항상 바뀌기 때문에 vis 매번 다시 생성 
    for vir in virpos: # Q 초기화 매번 필요 
        Q.append(vir)

    while Q:
        if nvirus <= safe: # pruning, 이것 때문에 Q 매번 다시 생성 필요 
            break
        cx, cy = Q.popleft()
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if 0<=nx<N and 0<=ny<M and not vis[nx][ny] and board[nx][ny]==0:
                vis[nx][ny] = True
                Q.append((nx, ny))
                nvirus -= 1
    if nvirus > safe:
        safe = nvirus

print(safe)        

