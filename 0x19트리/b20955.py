import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

rst = 0 
vis = [False]*(N+1)
for i in range(1, N+1):
    if not vis[i]:
        rst += 1
        V, E = 0, 0
        vis[i] = True
        Q = deque()
        Q.append(i)

        while Q:
            cur = Q.popleft()
            V += 1
            for nxt in adj[cur]:
                E += 1
                if not vis[nxt]:
                    vis[nxt] = True
                    Q.append(nxt)
        
        rst += (E//2 - (V-1))

print(rst-1)