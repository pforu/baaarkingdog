import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

def dijk(st):
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

    return d

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

main_d = dijk(X)

ans = 0
for i in range(1, N+1):
    d = dijk(i)
    ans = max(ans, d[X] + main_d[i])

print(ans)