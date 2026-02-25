import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

R, B, O = 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j]=='R':
            R = (i, j)
        elif board[i][j]=='B':
            B = (i, j)
        elif board[i][j]=='O':
            O = (i, j)

rst = 11
for p in product(range(4), repeat=10):
    rx, ry = R
    bx, by = B
    bef2i, bef1i = -1, -1
    stop = False

    for num, i in enumerate(p):
        if bef1i==i or (bef2i==i and bef1i%2==i%2):
            break
        bef2i, bef1i = bef1i, i
        
        befrx, befry, befbx, befby = rx, ry, bx, by

        dx, dy = DIRS[i]
        while board[bx+dx][by+dy] != '#':
            bx, by = bx+dx, by+dy
            if (bx, by)==O:
                stop = True
                break
        if stop: break

        while board[rx+dx][ry+dy] != '#':
            rx, ry = rx+dx, ry+dy
            if (rx, ry)==O:
                rst = min(rst, num+1)
                stop = True
                break
        if stop: break

        if rx==bx and ry==by:
            if (befrx < befbx and dx==1) or (befrx > befbx and dx==-1):
                # r이 위에 있는 상태에서 아래로 움직임, r이 아래에 있는 상태에서 위로 움직임 
                rx -= dx
            elif (befrx < befbx and dx==-1) or (befrx > befbx and dx==1):
                # r이 위에 있는 상태에서 위로 움직임, r이 아래에 있는 상태에서 아래로 움직임
                bx -= dx
            elif (befry < befby and dy==1) or (befry > befby and dy==-1):
                # r이 왼쪽에 있는 상태에서 오른쪽으로 움직임, r이 오른쪽에 있는 상태에서 왼쪽으로 움직임
                ry -= dy
            elif (befry < befby and dy==-1) or (befry > befby and dy==1):
                # r이 왼쪽에 있는 상태에서 왼쪽으로 움직임, r이 오른쪽에 있는 상태에서 오른쪽으로 움직임 
                by -= dy
            else:
                print('error')

print(-1 if rst==11 else rst)            