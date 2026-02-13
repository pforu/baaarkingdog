import sys
input = sys.stdin.readline
from collections import deque
# M <= N <= 1000이므로 그때그때 구하든 미리 구하든 시간복잡도 동일

def solve(cur, end, dist):
    # print(cur, end, dist)
    if cur==end:
        return dist
    for nxt, weight in adj[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            res = solve(nxt, end, dist + weight)
            if res is not None:
                return res
### 갈림길에서 함수가 for로 각각에 대해 실행되어 내려가야 할 때,
### return은 첫 함수가 내려갔다가 결과를 받아오자마자 그 층을 종료함

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, weight = map(int, input().split())
    adj[u].append((v, weight))
    adj[v].append((u, weight))

# p = [0]*(N+1)
# dfs(1) # 노드 사이의 거리만 구하므로 어떤 노드를 루트로 잡아도 괜찮음 
### 거슬러 올라가는 경우가 생길 수 있으므로, p 말고 vis 사용 

ans = []
for _ in range(M):
    u, v = map(int, input().split())
    vis = [False]*(N+1)
    vis[u] = True # 첫 노드 방문처리 잊지 말기 
    ans.append(solve(u, v, 0))
print('\n'.join(map(str, ans)))