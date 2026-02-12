import sys
input = sys.stdin.readline
from collections import deque
# 초기값 0, 표시는 -1, 1로

def solve(adj, V):
    mark = [0]*(V+1)
    vis = [False]*(V+1)
    Q = deque()
    for i in range(1, V+1):
        if not vis[i]:
            mark[i] = 1
            Q.append(i)

            while Q:
                cur = Q.popleft()
                vis[cur] = True # 뺄 때 방문표시를 해야 다 돌고 이분그래프 아닌지 판단 가능 

                for nxt in adj[cur]:
                    if not vis[nxt]:
                        # print(cur, mark[cur], nxt, mark[nxt])
                        if mark[nxt]==mark[cur]:
                            return False
                        if mark[nxt]==0:
                            mark[nxt] = -mark[cur]
                        Q.append(nxt)
    return True
                        
K = int(input())
ans = []
for _ in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    ans.append('YES' if solve(adj, V) else 'NO')

print('\n'.join(ans))