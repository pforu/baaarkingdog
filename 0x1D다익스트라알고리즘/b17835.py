### 바로 TLE, 시간복잡도 NMlogM
import sys
input = sys.stdin.readline
import heapq
# 여러 곳이면 가장 작은 번호 출력 
INF = int(1e9)

N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

items = set(map(int, input().split()))
max_dis, max_city = 0, 0

for i in (range(1, N+1)):
    if i in items:
        continue
    d = [INF]*(N+1)
    h = []
    d[i] = 0
    heapq.heappush(h, (d[i], i))

    while h:
        c_dis, c_num = heapq.heappop(h)
        if d[c_num]!=c_dis: continue
        for n_dis, n_num in adj[c_num]:
            if d[n_num] > c_dis + n_dis:
                d[n_num] = c_dis + n_dis
                heapq.heappush(h, (d[n_num], n_num))
    
    dis_to_item = min([d[x] for x in items])
    if dis_to_item > max_dis:
        max_dis, max_city = dis_to_item, i

print(max_city, max_dis, sep='\n')