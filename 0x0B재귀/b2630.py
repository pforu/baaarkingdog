import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)] # w:0, b:1

rst = [0]*2

def check(n, x, y):
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j]!=board[x][y]:
                return False
    return True

def func(n, x, y):
    if check(n, x, y):
        rst[board[x][y]] += 1
        return
    
    z = n//2
    for i in range(2):
        for j in range(2):
            func(z, x+i*z, y+j*z)

func(N, 0, 0)
print(rst[0], rst[1], sep='\n')