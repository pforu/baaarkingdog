import sys
input = sys.stdin.readline
from collections import deque

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

T = int(input())
rst = [0]*T

for idx in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1
    
    vis = [[False]*M for _ in range(N)]
    Q = deque()

    for i in range(N):
        for j in range(M):
            if not vis[i][j] and board[i][j] == 1:
                vis[i][j] = True
                Q.append((i, j))
                rst[idx] += 1

                while Q:
                    cx, cy = Q.popleft()

                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy

                        if 0<=nx<N and 0<=ny<M and not vis[nx][ny] and board[nx][ny]==1:
                            vis[nx][ny] = True
                            Q.append((nx, ny))

print("\n".join(map(str, rst)))