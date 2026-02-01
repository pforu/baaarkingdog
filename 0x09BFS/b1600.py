import sys
input = sys.stdin.readline
from collections import deque

K = int(input()) # 나이트 이동횟수 최대값 : 0~30
W, H = map(int, input().split()) # 1~200
board = [list(map(int, input().split())) for _ in range(H)] # 0 : 평지, 1 : 장애물
# 시작점과 도착점은 항상 평지
# 출력 : 동작수의 최솟값, 불가능할 경우 -1

KNIGHTS = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

# 벽부수기랑 좀 비슷
# 근데 이건 여러 번 가능하니까, 차원이 그만큼 많아야 되나?
# 그럼 그 차원을 상태 하나로 두고 dist나 vis에다가 한 차원을 더 더해서,
# 값(몇 번 나이트처럼 이동했는지)을 저장하면 되나?

vis = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]
# (x, y) 좌표에 리스트가 있음
# 인덱스 : 나이트가 쓰인 횟수, 값 : 전체 이동 횟수
Q = deque()
vis[0][0][0] = 0
Q.append((0, 0, 0))

while Q:
    cx, cy, ck = Q.popleft()
    if ck<K:
        for dx, dy in KNIGHTS:
            nx, ny, nk = cx + dx, cy + dy, ck+1
            if 0<=nx<H and 0<=ny<W and vis[nx][ny][nk]==-1 and board[nx][ny]==0:
                vis[nx][ny][nk] =  vis[cx][cy][ck] + 1
                Q.append((nx, ny, nk))

    for dx, dy in DIRS:
        nx, ny, nk = cx + dx, cy + dy, ck
        if 0<=nx<H and 0<=ny<W and vis[nx][ny][nk]==-1 and board[nx][ny]==0:
            vis[nx][ny][nk] =  vis[cx][cy][ck] + 1
            Q.append((nx, ny, nk))

rst = [x for x in vis[H-1][W-1] if x!=-1]
if rst:
    print(min(rst))
else:
    print(-1)

# 3% WA