import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

V, E = map(int, input().split())
k = int(input())
adj = [[] for _ in range(V+1)] # 모든 쌍 보는 게 아니라서 adj 필요 
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v)) # 가중치부터 넣는 것 주의 

d = [INF]*(V+1)
h = []

d[k] = 0
heapq.heappush(h, (d[k], k))
while h:
    cur_dis, cur_num = heapq.heappop(h) # 갈 수 있는 곳 중 최단 고르기 
    if d[cur_num]!=cur_dis: continue # 이미 더 최단거리인 것으로 덮였다면 건너뛰기 
    for nxt_dis, nxt_num in adj[cur_num]: # 덮인 게 아닌 cur은 확정, 여기서 뻗어야 최단 후보임 
        if d[nxt_num] > cur_dis + nxt_dis: # 여기를 거쳐 가는 게 더 빠르면 갱신 
            d[nxt_num] = cur_dis + nxt_dis
            heapq.heappush(h, (d[nxt_num], nxt_num)) # 갱신됐다면 새로운 최단이므로 후보에 넣기 

ans = [str(x) if x!=INF else 'INF' for x in d[1:]]
print('\n'.join(ans))
# if로 print 할지 말지 결정할(필터링) 때는 for문 뒤로, 
# if-else로 print할 값 변경할 때는 for문 앞으로 