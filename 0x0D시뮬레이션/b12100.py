# 구현 안 됨 

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def merge(lst):
    # lst = [0, 2, 0, 2, 8, 8, 0, 16]
    Q = deque()
    P = deque()
    for i in lst:
        if i!=0: Q.append(i)
    rst = []
    if len(Q)<2:
        while Q:
            rst.append(Q.popleft())
    while Q:
        while len(P)<2 and Q:
            P.append(Q.popleft())
        if len(P)==2:
            bef = P.popleft()
            cur = P[0]
            if bef==cur:
                rst.append(bef*2)
                P.popleft()
            else:
                rst.append(bef)
        else:
            while P:
                rst.append(P.popleft())
    return rst+[0]*(N-len(rst))

DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1)) #하 우 상 좌 
maxval = 0
for i in range(1<<2*5): # 5번의 이동이 가능한 모든 경우의 수 
    board2 = [row[:] for row in board]
    ans = []
    for p in range(5): # 5번의 이동 
        dir = i%4
        i //= 4
        for k in range(N): # 1번의 이동 
            lst = [0]*N
            DIRS2 = ((0, k), (k, 0), (N-1, k), (k, N-1))
            x, y = DIRS2[dir]
            dx, dy = DIRS[dir]
            for j in range(N): # 줄 생성 
                lst[j] = board2[x][y]
                x, y = x + dx, y + dy
            ans.append(merge(lst))
        board2 = [row[:] for row in ans]
    maxval = max(maxval, max(max(row) for row in board2))

print(maxval)