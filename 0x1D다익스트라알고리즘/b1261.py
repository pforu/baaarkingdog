import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

M, N = map(int, input().split()) # N, M 순서 항상 주의 
board = [[-1]*(N+1)] + [[-1] + list(map(int, input().strip())) for _ in range(N)]
# 1-indexed로 잘 맞추기, 특히 첫 행 []으로 감싸기 

d = [[INF]*(M+1) for _ in range(N+1)] # cost가 부순 벽의 개수 
h = []

d[1][1] = 0
heapq.heappush(h, (d[1][1], 1, 1))

while h:
    cur_cost, cx, cy = heapq.heappop(h)
    if d[cx][cy]!=cur_cost: continue
    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy
        if 1<=nx<=N and 1<=ny<=M and d[nx][ny] > cur_cost + board[nx][ny]:
            d[nx][ny] = cur_cost + board[nx][ny]
            heapq.heappush(h, (d[nx][ny], nx, ny))

print(d[N][M])
