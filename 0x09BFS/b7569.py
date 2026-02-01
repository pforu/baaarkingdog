import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

DIRS = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

dist = [[[-1]*M for _ in range(N)] for _ in range(H)]
Q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k]==1:
                dist[i][j][k] = 0
                Q.append((i, j, k))

while Q:
    cx, cy, cz = Q.popleft()

    for dx, dy, dz in DIRS:
        nx, ny, nz = cx + dx, cy + dy, cz + dz

        # 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
        if 0<=nx<H and 0<=ny<N and 0<=nz<M and dist[nx][ny][nz]==-1 and board[nx][ny][nz]==0:
            dist[nx][ny][nz] = dist[cx][cy][cz] + 1
            Q.append((nx, ny, nz))

rst = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k]!=-1 and dist[i][j][k]==-1: # 원래 있었는데 안 익었으면 
                print(-1)
                exit()
            rst = max(rst, dist[i][j][k])
print(rst)