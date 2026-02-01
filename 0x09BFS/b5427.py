import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0)) # 어차피 뭘 먼저 보든 거리는 똑같이 측정 

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불

def solve():
    W, H = map(int, input().split())
    board = [input().strip() for _ in range(H)]

    fire = [[-1]*W for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]
    Q = deque()

    # fire
    for i in range(H):
        for j in range(W):
            if board[i][j]=='*':
                fire[i][j] = 0
                Q.append((i, j))
    
    while Q:
        cx, cy = Q.popleft()

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy

            if 0<=nx<H and 0<=ny<W and fire[nx][ny]==-1 and board[nx][ny]!='#': # 벽만 아니면 됨 
                fire[nx][ny] = fire[cx][cy] + 1
                Q.append((nx, ny))

    # dist
    for i in range(H):
        for j in range(W):
            if board[i][j]=='@':
                dist[i][j] = 0
                Q.append((i, j))
    
    while Q:
        cx, cy = Q.popleft()

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            #탈출이랑 dist 분기를 따로 작성 필요 
            if nx<0 or nx>=H or ny<0 or ny>=W:
                print(dist[cx][cy] + 1)
                return

            if dist[nx][ny]==-1 and board[nx][ny]!='#':
                if fire[nx][ny] > dist[cx][cy] + 1 or fire[nx][ny]==-1: 
                    dist[nx][ny] = dist[cx][cy] + 1
                    Q.append((nx, ny))

    print("IMPOSSIBLE")

for _ in range(T):
    solve()