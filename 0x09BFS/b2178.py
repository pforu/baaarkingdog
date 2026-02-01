import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

dist = [[-1] * M for _ in range(N)]
Q = deque()

# 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

dist[0][0] = 0
Q.append((0, 0))

while Q:
    cx, cy = Q.popleft()

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny]==-1 and board[nx][ny]==1:
            dist[nx][ny] = dist[cx][cy] + 1
            Q.append((nx, ny))

# 칸을 셀 때에는 시작 위치와 도착 위치도 포함
print(dist[N-1][M-1]+1)