import sys
input = sys.stdin.readline

INF = int(1e9) # 보통 노드 개수(100) * 최대 가중치(100000)
N = int(input())
M = int(input())
d = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    d[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    d[u][v] = min(d[u][v], w)

for k in range(1, N+1): ### 거쳐가는 노드 k가 반드시 맨 바깥 루프
    for i in range(1, N+1):
        for j in range(1, N+1):
            if d[i][j] > d[i][k] + d[k][j]: # 비교연산자 방향 확인 
                d[i][j] = d[i][k] + d[k][j] # 대입 연산의 부하를 줄이기 위해 min 대신 비교 후 대입  

for i in range(1, N+1):
    for j in range(1, N+1):
        if d[i][j]==INF:
            d[i][j] = 0

for row in d[1:]: # 이차원배열 출력 기억해놓기
    print(*row[1:])