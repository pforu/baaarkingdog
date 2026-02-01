import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

fire = [[-1]*C for _ in range(R)]
dist = [[-1]*C for _ in range(R)]
Q = deque()

# fire
for i in range(R):
    for j in range(C):
        if board[i][j]=='F':
            fire[i][j] = 0 # 시작점 표시하기 
            Q.append((i, j))

while Q:
    cx, cy = Q.popleft()

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < R and 0 <= ny < C and fire[nx][ny]==-1 and board[nx][ny]!='#':
            # board[nx][ny]=='.' 이 아님, J도 갈 수 있음 
            fire[nx][ny] = fire[cx][cy] + 1
            Q.append((nx, ny))

# dist
for i in range(R):
    for j in range(C):
        if board[i][j]=='J':
            dist[i][j] = 0 # 시작점 표시하기 
            Q.append((i, j))

while Q:
    cx, cy = Q.popleft()

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        if nx < 0 or nx >= R or ny < 0 or ny >= C: # 벗어날 시 탈출성공 
            print(dist[cx][cy] + 1)
            exit()

        if dist[nx][ny]==-1 and board[nx][ny]!='#':
            # board[nx][ny]=='.' 이 아님, F도 갈 수 있음 
            if fire[nx][ny]==-1 or fire[nx][ny] > dist[cx][cy] + 1:
                # 불이 아예 안 오거나 / 지훈보다 늦음 : 초기값이 -1이므로 후자의 조건은 전자를 포함할 수 없음 
                dist[nx][ny] = dist[cx][cy] + 1
                Q.append((nx, ny))

print("IMPOSSIBLE")