import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

# 완전 탐색 후 검증은 입력값 작을 때 꼭 고려하기 
board = [list(0 if i=='Y' else 1 for i in input().strip()) for _ in range(5)]
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def search(comb):
    # 배열에 넣기 
    this = [[0]*5 for _ in range(5)]
    for k in comb:
        this[k//5][k%5] = 1
    # print(*this)
    
    # S>=4 검사
    sum = 0
    for i in range(5):
        for j in range(5):
            if this[i][j]==1 and board[i][j]==1:
                sum += 1
    # print(sum)
    if sum<4:
        return False
    
    # 인접 검사
    Q = deque()
    vis = [[False]*5 for _ in range(5)]
    cnt = 0

    # print(*this)
    for i in range(5):
        for j in range(5):
            if not vis[i][j] and this[i][j]==1: ### vis 검사를 안 해서 계속 여기서 False 반환하는 실수 
                if cnt>0:
                    return False
                cnt += 1
                Q.append((i, j))

                while Q:
                    cx, cy = Q.popleft()

                    for dx, dy in DIRS:
                        nx, ny = cx + dx, cy + dy

                        if 0<=nx<5 and 0<=ny<5 and not vis[nx][ny] and this[nx][ny]==1:
                            vis[nx][ny] = True
                            Q.append((nx, ny))
                # print(*vis)
    return True

rst = 0
# stop = 0
for c in combinations(range(25), 7):
    # if stop>0: break
    # stop += 1
    if search(c):
        rst += 1

print(rst)