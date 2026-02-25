import sys
input = sys.stdin.readline
from itertools import product, permutations
from collections import deque

DIRS = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
SE = (((0, 0, 0), (4, 4, 4)), ((0, 0, 4), (4, 4, 0)), ((0, 4, 0), (4, 0, 4)), ((0, 4, 4), (4, 0, 0)))

board = [[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]]
# 1은 참가자가 들어갈 수 있는 칸

def rotate(board, num):
    raw_tmp = [row[:] for row in board]
    tmp = [[0]*5 for _ in range(5)]
    for _ in range(num):
        for i in range(5):
            for j in range(5):
                tmp[5-1-j][i] = raw_tmp[i][j]
        raw_tmp = [row[:] for row in tmp]
    return [row[:] for row in raw_tmp]

for n in range(1, 4):
    board.append([rotate(board[0][i], n) for i in range(5)]) # 미리 rotate한 결과 저장하는 게 가장 중요
    # 다른 최적화 이전에, 값을 미리 저장해 둘 수 있는지 생각해보자 

def solve():
    rst = 150
    for pan in permutations(range(5)):
        for dir in product(range(4), repeat=5):

            maze = [board[dir[i]][pan[i]] for i in range(5)] # itertools 쓰는 법 더 익히기 

            if maze[0][0][0]==1 and maze[4][4][4]==1: # 출발점이 1일 때만 탐사 돌려야 함 
                dist = [[[-1]*5 for _ in range(5)] for _ in range(5)]
                Q = deque()

                dist[0][0][0] = 0
                Q.append((0, 0, 0))

                while Q:
                    cx, cy, cz = Q.popleft()
                    if cx==4 and cy==4 and cz==4:
                        break
                    for dx, dy, dz in DIRS:
                        nx, ny, nz = cx + dx, cy + dy, cz + dz
                        if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                            if dist[nx][ny][nz]==-1 and maze[nx][ny][nz]==1:
                                dist[nx][ny][nz] = dist[cx][cy][cz] + 1
                                Q.append((nx, ny, nz))

                if dist[4][4][4]!=-1:
                    rst = min(rst, dist[4][4][4])
                    if rst==12:
                        return rst # 1이 많으면 시간이 매우 길어짐, 최소거리 나오면 바로 중단 
    return rst

rst = solve()
print(-1 if rst==150 else rst)