import sys
input = sys.stdin.readline

N = int(input())
rst = [[0]*N for _ in range(N)]

def func(n, x, y):
    if n==3:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    continue
                rst[x+i][y+j] = 1
        return
    
    z = n//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            func(z, x+i*z, y+j*z)

func(N, 0, 0)

for i in range(N):
    for j in range(N):
        print('*' if rst[i][j]==1 else ' ', end='')
    print()