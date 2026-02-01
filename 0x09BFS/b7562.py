import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
rst = [0]*T
DIRS = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))


for i in range(T):
    L = int(input())
    curX, curY = map(int, input().split())
    nxtX, nxtY = map(int, input().split())

    dist = [[-1]*L for _ in range(L)]
    Q = deque()

    dist[curX][curY] = 0
    Q.append((curX, curY))

    while dist[nxtX][nxtY] == -1:
        cx, cy = Q.popleft()

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy

            if 0<=nx<L and 0<=ny<L and dist[nx][ny]==-1:
                dist[nx][ny] = dist[cx][cy] + 1
                Q.append((nx, ny))
    
    rst[i] = dist[nxtX][nxtY]

print("\n".join(map(str, rst)))