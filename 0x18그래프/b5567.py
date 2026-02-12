import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
adj = [[] for _ in range(N+2)]
vis = [False]*(N+2)
Q = deque()
for _ in range(M):
    u, v = map(int, input().split())
    if u==1:
        vis[v] = True # Q.append에는 무조건 vis/dist가 선행되는 것 잊지 말기 
        Q.append(v)
    adj[u].append(v)
    adj[v].append(u)

while Q:
    cur = Q.popleft()

    for nxt in adj[cur]:
        if not vis[nxt]:
            vis[nxt] = True

print(vis[2:].count(True))