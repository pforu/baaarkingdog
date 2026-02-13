import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6) ## 제발 까먹지 마 

def dfs(cur, weight):
    weight += comp[cur]
    rst[cur] = weight
    for nxt in adj[cur]:
        dfs(nxt, weight)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i, n in enumerate(map(int, input().split())):
    if n!=-1: adj[n].append(i+1)

comp = [0]*(N+1)
for i in range(M):
    num, w = map(int, input().split())
    comp[num] += w

rst = [0]*(N+1)
dfs(1, 0)

print(*rst[1:])