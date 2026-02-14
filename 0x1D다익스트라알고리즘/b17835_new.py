import sys
input = sys.stdin.readline
import heapq
### 다익스트라에서 NMlogM을 MlogM으로 줄이는 테크닉
# 1. 여러 개의 노드 중 아무데서나 출발해서 특정 목적지로 : 힙에 모든 시작점 넣고 시작
# 2. A 집단 노드 중 하나에서 B 집단 노드 중 하나로 : S>A, B>E 모두 연결 후 S>E 확인 
# 3. 모든 노드에서 특정 목적지로 : 모든 간선 방향을 뒤집어 목적지를 시작점으로 한 번 

# 이 문제의 경우, 1번과 3번을 동시에 사용 
INF = int(1e11) # 10만 * 10만 = 1e10

N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[v].append((w, u)) # 간선을 반대로 받기 
items = list(map(int, input().split()))

d = [INF]*(N+1)
h = []
for i in items: # 모든 면접장을 시작점으로 넣기 
    d[i] = 0
    heapq.heappush(h, (d[i], i))

while h:
    c_dis, c_num = heapq.heappop(h)
    if d[c_num]!=c_dis: continue
    for n_dis, n_num in adj[c_num]:
        if d[n_num] > c_dis + n_dis:
            d[n_num] = c_dis + n_dis
            heapq.heappush(h, (d[n_num], n_num))

max_dis, max_city = 0, 0
for c in range(1, N+1):
    if d[c] > max_dis:
        max_dis = d[c]
        max_city = c
print(max_city, max_dis, sep='\n')