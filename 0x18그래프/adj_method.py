import array
V, E = 5, 7

# 보통 1-indexed 사용

### 인접 행렬
# 연결 여부 반복적 확인, 간선 개수 많음, 간선 가중치 업데이트 반복적, 플로이드워셜
# 각 행을 비트마스킹 처리하는 방법도 존재 
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

# 방향 그래프
for _ in range(E):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1

# 무방향그래프
for _ in range(E):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1


### 인접 리스트
# 대부분의 표준 상황에 적합 
adj_list = array.array([[] for _ in range(V+1)])

# 방향 그래프
for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u].append(v)

# 무방향 그래프
for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# 방문할 수 있는 정점이 여러 개라면 번호가 작은 것부터 방문 : 정렬 
for i in range(1, V+1):
    adj_list[i].sort()