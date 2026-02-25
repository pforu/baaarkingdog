import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)] # 좌표는 0-indexed
ins = list(map(int, input().split())) # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

DIRS = ((0, 1), (0, -1), (-1, 0), (1, 0))

d = [0]*7 # 1-indexed

def swap(x, y):
    if board[x][y]==0:
        board[x][y] = d[6]
    else:
        d[6] = board[x][y]
        board[x][y] = 0
    return (x, y, d[1])

def roll(dir, x, y):
    dx, dy = DIRS[dir-1]
    if not (0<=x+dx<N and 0<=y+dy<M): return (-1, -1, -1)
    if dir==1:
        d[3], d[6], d[4], d[1] = d[1], d[3], d[6], d[4]
    elif dir==2:
        d[1], d[3], d[6], d[4] = d[3], d[6], d[4], d[1]
    elif dir==3:
        d[2], d[6], d[5], d[1] = d[1], d[2], d[6], d[5]
    else:
        d[1], d[2], d[6], d[5] = d[2], d[6], d[5], d[1]
    return swap(x+dx, y+dy) # return을 안 하면 swap()의 return값이 main으로 안 전해짐 

posx, posy = x, y
ans = []
for i in ins:
    ret = roll(i, posx, posy)
    if ret[0]!=-1:
        posx, posy = ret[0], ret[1]
        ans.append(ret[2])
print('\n'.join(map(str, ans)))