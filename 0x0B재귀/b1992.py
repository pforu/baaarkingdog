import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
rst = []

# 문제에 있는 예시가 예제와 같을 거라고 짐작하지 않기..

def check(n, x, y):
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j]!=board[x][y]:
                return False
    return True

def func(n, x, y):
    if check(n, x, y):
        rst.append(board[x][y])
        return
    z = n//2
    rst.append('(')
    for i in range(2):
        for j in range(2):
            func(z, x+i*z, y+j*z)
    rst.append(')')

func(N, 0, 0)
print(''.join(map(str, rst)))