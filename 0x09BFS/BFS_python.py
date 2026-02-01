import sys
input = sys.stdin.readline
from collections import deque

# 첫 칸이 가능한 시작점이라고 가정 
board = [
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

N, M = 7, 10
vis = [[False] * M for _ in range(N)]
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1)) #우하좌상 순 

Q = deque()
vis[0][0] = True
Q.append((0, 0))

while Q:
    cx, cy = Q.popleft()
    # print(f"({cx}, {cy}) -> ", end="")

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        # if not (0 <= nx < N and 0 <= ny < M): continue
        # if vis[nx][ny] or board[nx][ny] != 1: continue
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny] and board[nx][ny] == 1:
            vis[nx][ny] = True
            Q.append((nx, ny))