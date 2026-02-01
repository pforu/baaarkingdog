import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

vis = [[False] * M for _ in range(N)]
Q = deque()


if board[0][0] == 1:
    vis[0][0] = True
    Q.append((0, 0))

while Q:
    cx, cy = Q.popleft()

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny] and board[nx][ny] == 1:
            vis[nx][ny] = True
            Q.append((nx, ny))


# board = [list(map(int, input().strip())) for _ in range(N)]