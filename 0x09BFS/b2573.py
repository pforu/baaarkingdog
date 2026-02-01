import sys
input = sys.stdin.readline
from collections import deque

# 시간복잡도 : 원래 90만, 조건상 1만개를 10번 돌면 됨
# > 덩어리 판단 때문에 180만 됨

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
ONE = 0
OVER_TWO = 1
NOT_FOUND = -1

var = [[0]*M for _ in range(N)]

def find():
    # 덩어리 파악
    vis = [[False]*M for _ in range(N)]
    Q = deque()
    find = NOT_FOUND
    for i in range(N):
        for j in range(M):
            if not vis[i][j] and board[i][j]!=0:
                if find==ONE:
                    return OVER_TWO
                vis[i][j] = True
                Q.append((i, j))

                while Q:
                    cx, cy = Q.popleft()
                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy

                        if 0<=nx<N and 0<=ny<M and not vis[nx][ny] and board[nx][ny]!=0:
                            vis[nx][ny] = True
                            Q.append((nx, ny))
                find = ONE
    return find

year = 0

while True:
    year += 1
    # 빙산돌기 : 300*300*4 = 36만
    for i in range(N):
        for j in range(M):
            if board[i][j]!=0:
                for dx, dy in DIRS:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
                        var[i][j] -= 1
    # 빙산 녹이기 
    for i in range(N):
        for j in range(M):
            board[i][j] = max(0, board[i][j] + var[i][j])
            var[i][j] = 0

    # print(*board, sep='\n')
    # print()

    found = find()
    if found==OVER_TWO:
        print(year)
        break
    elif found==NOT_FOUND:
        print(0)
        break

# 굳이 오래 생각해서 제일 빠른 코드를 짤 필요 없음 
# 시간복잡도 계산이 중요한 이유