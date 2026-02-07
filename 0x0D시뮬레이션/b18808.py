import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
note = [[0]*M for _ in range(N)]

# 그냥 직접 이차원배열을 인자로 주고 반환하면서, 함수 안에서 실시간으로 R, C 계산하기 

def able(sti, x, y, r, c):
    for i in range(r):
        for j in range(c):
            if note[x+i][y+j]==1 and sti[i][j]==1:
                return False
            
    for i in range(r):
        for j in range(c):
            if sti[i][j]==1:
                note[x+i][y+j] = 1
    return True

def rotate(sti):
    r, c = len(sti), len(sti[0])
    tmp = [[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-1-i] = sti[i][j] # 오른쪽으로 90도 돌림 
    return tmp

def stick(sti):
    cur_sti = sti
    for _ in range(4):
        r, c = len(cur_sti), len(cur_sti[0])
        for i in range(N-r+1):
            for j in range(M-c+1):
                if able(cur_sti, i, j, r, c):
                    return
        cur_sti = rotate(cur_sti)

for _ in range(K):
    R, C = map(int, input().split())
    sti = [list(map(int, input().split())) for _ in range(R)]
    stick(sti)

cnt = 0
for i in range(N):
    for j in range(M):
        if note[i][j]==1:
            cnt += 1
# cnt = sum(row.count(1) for row in note)
print(cnt)