from collections import deque

V = 10

# bfs - 부모와 depth 배열 채우기 
adj = [[] for _ in range(V+1)]
parent = [0]*(V+1)
depth = [0]*(V+1)

def bfs(root):
    Q = deque()
    Q.append(root)
    while Q:
        cur = Q.popleft()
        print(cur)

        for nxt in adj[cur]:
            if parent[cur]!=nxt:
                parent[nxt] = cur
                depth[nxt] = depth[cur] + 1
                Q.append(nxt)

# dfs - 재귀
def dfs(cur):
    for nxt in adj[cur]:
        if parent[cur]!=nxt:
            parent[nxt] = cur
            depth[nxt] = depth[cur] + 1
            dfs(nxt)

# dfs - 재귀, 단순 순회
def dfs(cur, par):
    for nxt in adj[cur]:
        if par!=nxt:
            dfs(nxt, cur)

# dfs - 비재귀
def dfs(root):
    S = deque()
    S.append(root)
    while S:
        cur = S.pop()

        for nxt in adj[cur]:
            if parent[cur]!=nxt:
                parent[nxt] = cur
                depth[nxt] = depth[cur] + 1
                S.append(nxt)


# 이진 트리 - 레벨 순회: bfs
lc = [0]*(V+1)
rc = [0]*(V+1)
def bfs():
    Q = deque()
    Q.append(1)
    while Q:
        cur = Q.popleft()
        if lc[cur]: Q.append(lc[cur])
        if rc[cur]: Q.append(rc[cur])

# 이진 트리 - 전/중/후위 순회: dfs
def preorder(cur):
    print(cur)
    if lc[cur]: preorder(lc[cur])
    if rc[cur]: preorder(rc[cur])