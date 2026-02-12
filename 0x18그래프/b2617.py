import sys
input = sys.stdin.readline
from collections import deque

def solve(adj, N, bound):
    cnt = 0 
    for i in range(1, N+1):
        vis = [False]*(N+1)
        Q = deque()
        vis[i] = True
        Q.append(i)

        while Q:
            cur = Q.popleft()

            for nxt in adj[cur]:
                if not vis[nxt]:
                    vis[nxt] = True
                    Q.append(nxt)
        # print(vis.count(True)-1) # 예제를 직접 손으로 풀어봤으면 디버깅에 좋음
        if vis.count(True)-1>=bound: # 자기는 빼는 거 잊지 말기 
            cnt += 1
    # print()
    return cnt


N, M = map(int, input().split())
bound = (N+1)//2
adj1 = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj1[u].append(v)
    adj2[v].append(u)
    
print(solve(adj1, N, bound) + solve(adj2, N, bound))