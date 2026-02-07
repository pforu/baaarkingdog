import sys
input = sys.stdin.readline
from itertools import product

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

N, M = map(int, input().split())
board_raw = [list(map(int, input().split())) for _ in range(N)]
rst = 0
cctv = []
for i in range(N):
    for j in range(M):
        if board_raw[i][j]==0:
            rst += 1
        elif board_raw[i][j]!=6:
            cctv.append((i, j, board_raw[i][j]))

def upd(x, y, dir):
    dir %= 4
    while True:
        x += DIRS[dir][0]
        y += DIRS[dir][1]
        if (x<0 or x>=N or y<0 or y>=M) or board[x][y]==6: return
        if board[x][y]!=0: continue
        board[x][y] = -1

ranges = [] # 각 변수가 가질 수 있는 값의 개수만큼 range 리스트 생성 
for _, _, type in cctv:
    types = range(1) if type==5 else range(2) if type==2 else range(4)
    ranges.append(types)

for dirs in product(*ranges): # 언패킹으로 넣기 
    board = [row[:] for row in board_raw]
    for i, dir in enumerate(dirs): # enumerate로 몇 번째 변수가 무슨 값 가지는지 뽑기 
        x, y, type = cctv[i]
        if type==1:
            upd(x, y, dir)
        elif type==2:
            upd(x, y, dir)
            upd(x, y, dir+2)
        elif type==3:
            upd(x, y, dir)
            upd(x, y, dir+1)
        elif type==4:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
        else:
            upd(x, y, dir)
            upd(x, y, dir+1)
            upd(x, y, dir+2)
            upd(x, y, dir+3)

    rst = min(rst, sum(row.count(0) for row in board))

print(rst)