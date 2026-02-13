import sys
input = sys.stdin.readline

INF = 200000
N, M = map(int, input().split())
d = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    d[u][v] = min(d[u][v], w)

for i in range(1, N+1):
    d[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

K = int(input())
city = list(map(int, input().split()))

rst = []
for x in range(1, N+1):
    max_round = 0
    city_able = True
    for c in city:
        round = d[x][c] + d[c][x]
        if round>=INF:
            city_able = False
            break
        max_round = max(round, max_round)
    if city_able:
        rst.append((max_round, x))
rst.sort()
idx = 0
while idx<N and rst[idx][0]==rst[0][0]:
    print(rst[idx][1], end=' ')
    idx += 1