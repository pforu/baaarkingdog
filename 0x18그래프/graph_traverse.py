import sys
from collections import deque

V, E = 5, 7

### BFS - vis
adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

def bfs():
    Q = deque()
    Q.append(1)
    vis[1] = True

    while Q:
        cur = Q.popleft()

        for nxt in adj[cur]:
            if not vis[nxt]:
                Q.append(nxt)
                vis[nxt] = True


### BFS - dist
adj = [[] for _ in range(V+1)]
dist = [-1]*(V+1)

def bfs():
    Q = deque()
    Q.append(1)
    dist[1] = 0

    while Q:
        cur = Q.popleft()
        
        for nxt in adj[cur]:
            if dist[nxt]==-1:
                Q.append(nxt)
                dist[nxt] = dist[cur] + 1      


### BFS - 연결그래프x
adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

def bfs():
    Q = deque()
    for i in range(1, V+1):
        if not vis[i]: # 통과하면 연결 요소 개수 +1
            Q.append(i)
            vis[i] = True

            while Q:
                cur = Q.popleft()

                for nxt in adj[cur]:
                    if not vis[nxt]:
                        Q.append(nxt)
                        vis[nxt] = True  


### DFS - 비재귀, 이상한 순서(순회는 됨)
adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

def dfs():
    S = deque()
    S.append(1)
    vis[1] = True

    while S:
        cur = S.pop()

        for nxt in adj[cur]:
            if not vis[nxt]:
                S.append(nxt)
                vis[nxt] = True  


### DFS - 재귀 
# 최대 재귀 깊이 초과 풀어두기 - 보통 정점 개수 * 10 
sys.setrecursionlimit(10**6)

adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

def dfs(cur):
    vis[cur] = True
    for nxt in adj[cur]:
        if not vis[nxt]:
            dfs(nxt)


### DFS - 비재귀, 재귀와 순서 동일 
adj = [[] for _ in range(V+1)]
vis = [False]*(V+1)

def dfs():
    S = deque()
    S.append(1)

    while S:
        cur = S.pop()
        if not vis[cur]:
            vis[cur] = True

            for nxt in adj[cur]:
                if not vis[nxt]:
                    S.append(nxt)
                    vis[nxt] = True 