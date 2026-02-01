import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 0은 바다, 1은 육지

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 원래 왔던 길도 여기 포함되어 버림, 어디서 왔는지 정보추가(방향 말고 섬)
dist = [[[-1]*2 for _ in range(N)] for _ in range(N)] # 각 좌표에 [거리, 방향]
isl = [[-1]*N for _ in range(N)] # 섬 라벨링 용도 
Q_sh, Q_isl = deque(), deque() # 해안선, 섬

# 섬 라벨링 
idx = -1
for i in range(N):
    for j in range(N):
        if isl[i][j]==-1 and board[i][j]==1:
            idx+=1
            isl[i][j] = idx
            Q_isl.append((i, j))

            while Q_isl:
                cx, cy = Q_isl.popleft()
                for dx, dy in DIRS:
                    nx, ny = cx+dx, cy+dy
                    if 0<=nx<N and 0<=ny<N and isl[nx][ny]==-1 and board[nx][ny]==1:
                        # 다음이 안 본 위치고, 다음이 섬 
                        isl[nx][ny] = idx
                        Q_isl.append((nx, ny))


# 해안선 넣기 
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            for dx, dy in DIRS:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N and dist[i][j][0]==-1 and board[nx][ny]==0:
                        # 여기가 안 본 해안이고, 다음이 바다 
                        dist[i][j] = [0, isl[i][j]]
                        Q_sh.append((i, j))

# 섬 잇기 
rst = N*3
while Q_sh:
    cx, cy = Q_sh.popleft()
    for dx, dy in DIRS:
        nx, ny = cx+dx, cy+dy

        if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
            # 다음이 바다인데 
            if dist[nx][ny][1]==-1: # 누가 먼저 안 봤으면 
                dist[nx][ny] = [dist[cx][cy][0] + 1, dist[cx][cy][1]]
                Q_sh.append((nx, ny))
            elif dist[nx][ny][1]!= dist[cx][cy][1]: # 왔던 적 있는데 다른 섬에서 온 거면 
                rst = min(rst, dist[cx][cy][0] + dist[nx][ny][0])
                
print(rst)               