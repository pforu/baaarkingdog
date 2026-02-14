import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
st, end = map(int, input().split())

d = [INF]*(N+1)
pre = [0]*(N+1) # pre 배열, 플로이드와 반대로 마지막에서 거슬러 올라감 
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
            pre[nxt_num] = cur_num # pre 갱신 

route = []
cur = end # 따라가기 
while cur!=st: 
    route.append(cur)
    cur = pre[cur]
route.append(cur)

print(d[end])
print(len(route))
print(*route[::-1]) # == reversed(route)
