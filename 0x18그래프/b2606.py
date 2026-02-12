import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
vis = [False]*(V+1)
Q = deque()

vis[1] = True
Q.append(1)

rst = -1
while Q:
    cur = Q.popleft()
    rst += 1

    for nxt in adj[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            Q.append(nxt)

print(rst)