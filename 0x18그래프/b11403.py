import sys
input = sys.stdin.readline
from collections import deque
# 방향 그래프인지 아닌지 등, 문제 조건 잘 읽기 

N = int(input())
adj = [[-1]*(N+1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]
# print(adj)
# N개의 정점에 대해, 각 정점에서 시작하면 중간에 1~N번째 정점을 거치는지 확인
# dfs N*N for N -> 100만

ans = []
for i in range(1, N+1):
    vis = [False]*(N+1)
    Q = deque()

    Q.append(i)

    while Q:
        cur = Q.popleft()

        for j in range(1, N+1):
            if not vis[j] and adj[cur][j]==1:
                vis[j] = True
                Q.append(j)
    
    ans.append(vis[1:])

for row in ans:
    print(' '.join(map(str, [1 if cell else 0 for cell in row])))