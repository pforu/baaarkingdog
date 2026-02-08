import sys
input = sys.stdin.readline
from collections import deque

N, M = 12, 6
board_raw = [list(input().strip()) for _ in range(N)]
board = [row[:] for row in board_raw]

def rotate():
    global board
    r, c = len(board), len(board[0])

    tmp = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-1-i] = board[i][j]
    board = [row[:] for row in tmp]

def pop():
    global board
    r, c = len(board), len(board[0])

    Q = deque()
    DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
    vis = [[False]*c for _ in range(r)]
    puyo = False

    for i in range(r):
        for j in range(c):
            if board[i][j]=='.':
                break
            if not vis[i][j]:
                cur = board[i][j]
                vis[i][j] = True
                Q.append((i, j))
                route = [(i, j)]

                while Q:
                    cx, cy = Q.popleft()
                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy
                        if 0<=nx<r and 0<=ny<c and not vis[nx][ny] and board[nx][ny]==cur:
                            vis[nx][ny] = True
                            Q.append((nx, ny))
                            route.append((nx, ny))

                if len(route)>=4:
                    puyo = True
                    for x, y in route:
                        board[x][y] = '0'
    return puyo


def fall():
    global board
    r, c = len(board), len(board[0])

    for i in range(r):
        tmp = ['.']*c
        idx = 0
        for j in range(c):
            cur = board[i][j]
            if cur=='.':
                break
            elif cur=='0':
                continue
            else:
                tmp[idx] = cur
                idx += 1
        board[i] = tmp[:]

rst = 0
rotate()
while pop():
    fall()
    rst += 1
print(rst)