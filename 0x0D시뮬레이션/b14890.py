import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def solve(lst):
    vis = [False]*N
    i = 1
    while i<N:
        if lst[i-1]>lst[i]:
            h = lst[i-1]
            for j in range(L):
                n = i+j
                if not 0<=n<N or lst[n]!=h-1 or vis[n]: # 조건과 범위 항상 주의 
                    return 0
                vis[i+j] = True
            i += (L-1)
        elif lst[i-1]<lst[i]:
            h = lst[i]
            for j in range(L):
                n = i-1-j
                if not 0<=n<N or lst[n]!=h-1 or vis[n]:
                    return 0
                vis[i-1-j] = True
        i += 1
    return 1

def rotate(board):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[j][i]
    return [row[:] for row in tmp]

ans = 0
for _ in range(2):
    for lst in board:
        ans += solve(lst)
    board = rotate(board)
print(ans)