import sys
input = sys.stdin.readline

INF = 2000
N, M, R = map(int, input().split())
item = [0] + list(map(int, input().split())) # 1-indexed로 설정
d = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(R):
    u, v, w = map(int, input().split())
    d[u][v] = min(d[u][v], w) # 초기화만 양방향으로 해두면 플로이드 돌면서는 알아서 같은 값 
    d[v][u] = min(d[v][u], w)

for i in range(1, N+1):
    d[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

max_items = [0]*(N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if d[i][j]<=M:
            max_items[i] += item[j]

print(max(max_items))