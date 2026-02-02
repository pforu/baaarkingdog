import sys
input = sys.stdin.readline

N = int(input())
# N-1 * 2
board = [[0]*(N*2-1) for _ in range(N)]

def func(n, x, y):
    if n==3:
        for i in range(3):
            for j in range(5):
                if (i==0 and j==2) or (i==1 and j%2==1) or (i==2):
                    board[x+i][y-2+j] = 1
        return
    # 2>1:3, 4>2:6, 8>4:12
    z = n//2
    func(z, x, y)
    func(z, x+z, y-z)
    func(z, x+z, y+z)

func(N, 0, N-1)

ans = []
for row in board:
    ans.append("".join('*' if cell else ' ' for cell in row))
print("\n".join(ans))

# for i in range(N):
#     for j in range(N*2-1):
#         print('*' if board[i][j]==1 else ' ', end='')
#     print()