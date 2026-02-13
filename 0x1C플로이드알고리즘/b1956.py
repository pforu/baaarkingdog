import sys
input = sys.stdin.readline

INF = 5000000

V, E = map(int, input().split())
d = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if w < d[u][v]: # 최적화 
        d[u][v] = w

for k in range(1, V+1):
    for i in range(1, V+1):
        if d[i][k]==INF: # 경유지로 가는 길 자체가 없으면 넘기기 
            continue
        for j in range(1, V+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

cost = INF
for i in range(1, V+1):
    if d[i][i]!=INF: # or, nxt[i][i]!=0
        cost = min(cost, d[i][i])

print(cost if cost!=INF else -1)