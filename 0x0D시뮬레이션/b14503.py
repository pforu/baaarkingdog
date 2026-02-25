import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 0은 청소안된빈칸, 1은벽 

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 웬만하면 준 대로 쓰고 나중에 구현할 때 활용 
# 활용하기 편하자고 여기서 비틀어두면 나중에 원래대로 써야 될 때 헷갈림 

vis = [[False]*M for _ in range(N)]
Q = deque()

vis[r][c] = True
Q.append((r, c))

x, y, dir = r, c, d
while True:
    # 1
    if not vis[x][y] and board[x][y]==0:
        vis[x][y] = True
    # 2
    found = False
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if not vis[nx][ny] and board[nx][ny]==0:
            found = True
            break
    if not found:
        x, y = x+DIRS[(dir+2)%4][0], y+DIRS[(dir+2)%4][1] # 후진 구현 잘 하기 
        if board[x][y]==1:
            break
    # 3
    else:
        dir = (dir-1 + 4)%4
        nx, ny = x+DIRS[dir][0], y+DIRS[dir][1]
        if not vis[nx][ny] and board[nx][ny]==0:
            x, y = nx, ny

rst = 0
for i in range(N):
    for j in range(M):
        if vis[i][j] and board[i][j]==0:
            rst += 1
print(rst)