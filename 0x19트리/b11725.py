import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(V-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u) # 둘 다 추가하는 게 맞음 

p = [0]*(V+1)
Q = deque()
Q.append(1)

while Q:
    cur = Q.popleft()

    for nxt in adj[cur]:
        if p[cur]!=nxt: # 잘 생각 
            p[nxt] = cur
            Q.append(nxt)

print('\n'.join(map(str, p[2:])))