### 이상한 코드 
# bfs 벽 부수기처럼 상태를 저장하려고 함 
import sys
input = sys.stdin.readline
import heapq
# 양방향, 한 골목에서 내야 하는 최대 요금을 최소화, 목표 지점을 갈 수 없다면 -1
INF = int(1e15) # 10만개 * 10^9원

N, M, A, B, C = map(int, input().split())
adj = [[-1]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w

d = [[INF]*(N+1) for _ in range(200)]
pre = [[0]*(N+1) for _ in range(200)]
h = []

stat = 0
d[stat][A] = 0
heapq.heappush(h, (d[stat][A], A))

while h:
    cd, cn = heapq.heappop(h)
    if d[stat][cn]!=cd:
        stat += 1
    for nn, nd in enumerate(adj[cn]):
        if nn==-1: continue
        if d[stat][nn] > cd + nd:
            d[stat][nn] = cd + nd
            pre[stat][nn] = cn
            heapq.heappush(h, (d[stat][nn], nn))

rst = -1
for i in range(200):
    if d[i][B] <= C:
        cur = B
        max_money = 0
        while B!=A:
            max_money = max(max_money, adj[cur][pre[cur]])
            cur = pre[cur]
        max_money = max(max_money, adj[cur][pre[cur]])
        rst = min(rst, max_money)
print(rst)