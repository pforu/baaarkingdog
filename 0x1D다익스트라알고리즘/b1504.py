import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

def dijk(st, en):
    d = [INF]*(N+1)
    h = []
    d[st] = 0
    heapq.heappush(h, (d[st], st))
    while h:
        cur_dis, cur_num = heapq.heappop(h)
        if d[cur_num]!=cur_dis: continue
        for nxt_dis, nxt_num in adj[cur_num]:
            if d[nxt_num] > cur_dis + nxt_dis:
                d[nxt_num] = cur_dis + nxt_dis
                heapq.heappush(h, (d[nxt_num], nxt_num))

    return d[en]



N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))
V1, V2 = map(int, input().split())
# 뭘 먼저 방문해야 하는지는 명시되어 있지 않다는 것 주의 
rst = min(dijk(1, V1) + dijk(V1, V2) + dijk(V2, N), dijk(1, V2) + dijk(V2, V1) + dijk(V1, N))
print(rst if rst<INF else -1)