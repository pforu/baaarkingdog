import sys
input = sys.stdin.readline
from collections import deque
# 트리 필요충분 : 아래 중 2가지
# 1. 연결 그래프
# 2. 사이클이 없음
# 3. 간선 개수가 V-1

ans = []
while True:
    N, M = map(int, input().split())
    if N==0:
        break
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    rst = 0
    vis = [False]*(N+1)
    Q = deque()
    for i in range(1, N+1):
        v, e = 0, 0
        if not vis[i]:
            vis[i] = True
            Q.append(i)

            while Q:
                cur = Q.popleft()
                v += 1
                for nxt in adj[cur]:
                    e += 1
                    if not vis[nxt]:
                        vis[nxt] = True
                        Q.append(nxt)
        if e//2 == v-1:
            rst += 1
    ans.append(rst)

for i, val in enumerate(ans):
    print(f"Case {i+1}: ", end='')
    if val==0:
        print("No trees.")
    elif val==1:
        print("There is one tree.")
    else:
        print(f"A forest of {val} trees.")