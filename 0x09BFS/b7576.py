import sys
input = sys.stdin.readline
from collections import deque

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수 : 다른 문제도 행, 열, 높이 입력 순서 주의 
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

dist = [[-1] * M for _ in range(N)]
Q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j]==1: # 처음에 다 넣는 거니까 방문하지 않았는지 체크 필요 없음 
            dist[i][j] = 0
            Q.append((i, j))
            
while Q: # 시작점 다 넣은 상태로 동시 확산, 위치는 거리 순으로 큐에 존재하게 됨 
    cx, cy = Q.popleft()

    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny]==-1 and board[nx][ny]==0:
            dist[nx][ny] = dist[cx][cy] + 1
            Q.append((nx, ny))

# 토마토가 모두 익을 때까지의 최소 날짜 출력 
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j]==0 and dist[i][j]==-1: # 익지 않았던 토마토인데 끝나고도 못 익음 
            print(-1)
            exit()
        ans = max(ans, dist[i][j]) # 매번 최대거리 갱신, 초기값 0 

print(ans) # 다 익은 토마토로 시작했을 경우 dist가 다 -1이어서 max는 0 

# 이차원배열의 max : max(max(row) for row in dist)
# 이차원배열의 any : any(-1 in row for row in dist)