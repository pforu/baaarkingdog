import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_cycle_path(curr, adj, visited, in_recursion, parent):
    visited[curr] = True
    in_recursion[curr] = True
    
    for neighbor in adj[curr]:
        if not visited[neighbor]:
            parent[neighbor] = curr # 어디서 왔는지 기록
            res = find_cycle_path(neighbor, adj, visited, in_recursion, parent)
            if res: return res # 사이클 찾으면 즉시 종료
            
        elif in_recursion[neighbor]:
            # 사이클 발견! 역추적 시작
            cycle = []
            temp = curr
            while temp != neighbor:
                cycle.append(temp)
                temp = parent[temp]
            cycle.append(neighbor)
            return cycle[::-1] # 순서대로 정렬
            
    in_recursion[curr] = False
    return None

# 설정 및 실행
V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)

visited = [False] * (V + 1)
in_recursion = [False] * (V + 1)
parent = [0] * (V + 1)
all_cycles = []

for i in range(1, V + 1):
    if not visited[i]:
        result = find_cycle_path(i, adj, visited, in_recursion, parent)
        if result:
            all_cycles.append(result)

print("찾은 사이클들:", all_cycles)