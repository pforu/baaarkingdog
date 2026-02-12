import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
while True:
    u, v = map(int, input().split())
    if u==-1:
        break
    adj[u].append(v)
    adj[v].append(u)

rst = []
for i in range(1, N+1):
    dist = [-1]*(N+1)
    Q = deque()

    dist[i] = 0
    Q.append(i)
    while Q:
        cur = Q.popleft()

        for nxt in adj[cur]:
            if dist[nxt]==-1:
                dist[nxt] = dist[cur] + 1
                Q.append(nxt)

    rst.append((max(dist), i))
rst.sort()

score = rst[0][0]
cnt = 0
ans = []
for val, num in rst:
    if val!=score:
        break
    ans.append(num)
    cnt += 1

print(score, cnt)
print(' '.join(map(str, ans)))