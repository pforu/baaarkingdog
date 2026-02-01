import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [input().strip() for _ in range(N)]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

vis = [[False]*N for _ in range(N)]
Q = deque()

cols = ['R', 'G']
rst = [0, 0]
# not 
for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            vis[i][j] = True
            Q.append((i, j))
            col = board[i][j]
            rst[0] += 1

            while Q:
                cx, cy = Q.popleft()

                for dx, dy in DIRS:
                    nx, ny = cx + dx, cy + dy

                    if 0<=nx<N and 0<=ny<N and not vis[nx][ny] and board[nx][ny]==col:
                        vis[nx][ny] = True
                        Q.append((nx, ny))

vis = [[False]*N for _ in range(N)]

# is
for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            vis[i][j] = True
            Q.append((i, j))
            col = board[i][j]
            rst[1] += 1

            while Q:
                cx, cy = Q.popleft()

                for dx, dy in DIRS:
                    nx, ny = cx + dx, cy + dy

                    if 0<=nx<N and 0<=ny<N and not vis[nx][ny]:
                        if (col in cols and board[nx][ny] in cols) or (col=='B' and board[nx][ny]=='B'):
                            vis[nx][ny] = True
                            Q.append((nx, ny))

print(*rst)                            