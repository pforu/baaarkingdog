import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

vis = [False]*(V+1)
Q = deque()

rst = 0
for i in range(1, V+1):
    if not vis[i]:
        vis[i] = True
        Q.append(i)
        rst += 1

        while Q:
            cur = Q.popleft()

            for nxt in adj[cur]:
                if not vis[nxt]:
                    vis[nxt] = True
                    Q.append(nxt)

print(rst)