import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
d = [[INF]*(N+1) for _ in range(N+1)]
nxt = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M): # 간선 개수만큼 받기
    u, v, w = map(int, input().split())
    d[u][v] = min(d[u][v], w)
    nxt[u][v] = v # u에서 v로 다른 정점을 거치지 않고 가려면 일단 v를 가야 함 

for i in range(1, N+1): ### 초기화 까먹지 말기 
    d[i][i] = 0

for k in range(1, N+1): # d[i][j]: 1~k의 노드만 경유지로 썼을 때 최단거리 
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, N+1):
    for j in range(1, N+1):
        if d[i][j]==INF:
            d[i][j] = 0

for row in d[1:]:
    print(*row[1:])

# out_ans = []
for i in range(1, N+1):
    ans = []
    for j in range(1, N+1):
        if nxt[i][j]==0 or i==j:
            ans.append("0")
            continue
        # rst = [0]
        rst = []
        k = i
        while k!=j:
            rst.append(k)
            k = nxt[k][j]
        rst.append(j)
        # rst[0] = len(rst)-1
        ans.append(f"{len(rst)} {' '.join(map(str, rst))}")
    print('\n'.join(ans)) ## 100번 출력이므로 아래처럼 할 필요 없음 
    # out_ans.append('\n'.join(ans))
# print('\n'.join(out_ans))

# print('\n'.join(' '.join(map(str, row)) for row in ans))
# 미리미리 묶어두기
