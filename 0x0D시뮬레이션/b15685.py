import sys
input = sys.stdin.readline

SIZE = 101 # 0~100이므로 
DIRS = ((0, 1), (-1, 0), (0, -1), (1, 0)) # 주어진 y, x 순으로 

N = int(input())
board = [[False]*SIZE for _ in range(SIZE)]
for _ in range(N):

    x, y, dir, gen = map(int, input().split())
    routes = [dir%4]
    for _ in range(gen): # 경로 전체 지정 후
        tmp = []
        for i in routes[::-1]:
            tmp.append((i+1)%4)
        routes.extend(tmp)

    board[y][x] = True
    for i in routes: # 실제로 움직이기 
        dy, dx = DIRS[i]
        y, x = y+dy, x+dx
        # print((x, y)) # 내가 실제로 파악하는 위치 
        board[y][x] = True
        
    # 첫 코드는 매번 새로운 경로 덧붙일 때마다 움직였음

cnt = 0
for i in range(SIZE-1):
    for j in range(SIZE-1):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            cnt += 1
print(cnt)