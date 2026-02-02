import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

rst = [0]*3

def check(n, x, y):
    for i in range(n): # 같은 숫자인지 
        for j in range(n):
            if board[x+i][y+j]!=board[x][y]:
                return False
    return True


def func(n, x, y):
    if check(n, x, y):
        rst[board[x][y] + 1] += 1
        return
    
    z = n//3
    for i in range(3): # 9개의 각 꼭짓점마다 재귀 돌리기 
        for j in range(3):
            func(z, x+i*z, y+j*z)

func(N, 0, 0)
print('\n'.join(map(str, rst)))