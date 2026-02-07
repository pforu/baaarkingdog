import sys
input = sys.stdin.readline
# 주의해서 잘 더할 것, 끝 부분의 예외처리 특히 주의 

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
d = [board[0][0]]
for i in range(1, N):
    tmp = [d[0] + board[i][0]] + [0]*(i-1) + [d[-1] + board[i][-1]]
    for j in range(1, i):
        tmp[j] = max(d[j-1], d[j]) + board[i][j]
    d = tmp[:]
print(max(d))