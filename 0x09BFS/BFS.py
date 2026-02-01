import sys
input = sys.stdin.readline
from collections import deque

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
vis = [[False]*M for _ in range(N)] #False로 선언? 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = deque()
# if board[0][0]==1: 첫 칸이 가능한 시작점이라고 가정 
vis[0][0] = 1
Q.append((0, 0))

while Q:
    cx, cy = Q.popleft()
    # print(f"({cx}, {cy}) -> ", end="")

    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if vis[nx][ny] or board[nx][ny] != 1: continue

        vis[nx][ny] = True
        Q.append((nx, ny))