import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)] # 정점+1개 설정 
for _ in range(M): # 간선 개수만큼 
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
for i in range(1, N+1): # 1 ~ 정점+1
    adj[i].sort()


def dfs(vis, cur):
    ans_dfs.append(cur)
    vis[cur] = True
    for nxt in adj[cur]:
        if not vis[nxt]:
            dfs(vis, nxt)

def bfs(vis):
    Q = deque()
    vis[V] = True
    Q.append(V)

    while Q:
        cur = Q.popleft()
        ans_bfs.append(cur)

        for nxt in adj[cur]:
            if not vis[nxt]:
                vis[nxt] = True
                Q.append(nxt)

ans_dfs = []
ans_bfs = []

vis = [False]*(N+1)
dfs(vis, V)
vis = [False]*(N+1)
bfs(vis)

print(' '.join(map(str, ans_dfs)))
print(' '.join(map(str, ans_bfs)))