import sys
input = sys.stdin.readline
from itertools import product

N = int(input())
board_raw = [list(map(int, input().split())) for _ in range(N)]

# 함수화를 잘 하자
# 판 전체를 돌릴 수 있다 
# itertools로 완탐하면 백트래킹보다 느리지만 더 간결해진다 
# 순차적 사고, 어떤 일이 벌어지는지 상상하기

def rotate():
    global board
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N-1-i] = board[i][j] # 오른쪽으로 90도 돌림 
    board = [row[:] for row in tmp]

def tilt(dir):
    for _ in range(dir): rotate()
    for i in range(N):
        tilted = [0]*N
        idx = 0
        for j in range(N):
            if board[i][j]==0: continue 

            if tilted[idx]==0: ### 블록이 들어감 
                tilted[idx] = board[i][j]
            elif tilted[idx] == board[i][j]: ### merge
                tilted[idx] *= 2
                idx += 1 # 다음 블록은 다음 칸에 들어올 수 있음 
            else: ### 수가 달라서 merge 불가  
                idx += 1 # 다음 칸에 
                tilted[idx] = board[i][j] # 블록 들어감 

        for j in range(N):
            board[i][j] = tilted[j]

maxblock = 0
for dirs in product(range(4), repeat=5):
    board = [row[:] for row in board_raw]
    for dir in dirs:
        tilt(dir)
    maxblock = max(maxblock, max(max(row) for row in board))
print(maxblock)