import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # dfs 쓸 거면 꼭 설정 

N, R, Q = map(int, input().split())
sub = [0]*(N+1)
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

p = [0]*(N+1)
def dfs(cur):
    rst = 1 # 본인 포함 
    for nxt in adj[cur]:
        if p[cur]!=nxt:
            p[nxt] = cur
            rst += dfs(nxt)
    sub[cur] = rst
    return rst

dfs(R)

q = [int(input()) for _ in range(Q)]
ans = [sub[i] for i in q]
print('\n'.join(map(str, ans)))