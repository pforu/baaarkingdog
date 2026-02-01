import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

vis = [[False] * M for _ in range(N)]
Q = deque()

rst = []

for i in range(N):
    for j in range(M):
        if not vis[i][j] and board[i][j] == 1:
            vis[i][j] = True
            Q.append((i, j))
            rst.append(1)
            
            while Q:
                cx, cy = Q.popleft()

                for dx, dy in DIRS:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny] and board[nx][ny] == 1:
                        vis[nx][ny] = True
                        Q.append((nx, ny))
                        rst[-1] += 1

print(len(rst), max(rst), sep='\n') if rst else print(0, 0, sep='\n')