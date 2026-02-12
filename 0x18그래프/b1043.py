import sys
input = sys.stdin.readline
from collections import deque
# 사람들을 두 덩어리(연결요소 2개)로 나누는 것
# 관계 저장에 파티도 노드로 추가, bipartite graph(이분그래프)

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
adj = [[] for _ in range(200)]
for i in range(1, M+1):
    party = 100+i
    people = list(map(int, input().split()))[1:]
    for per in people:
        adj[party].append(per)
        adj[per].append(party)
    
vis = [False]*200
Q = deque()
for i in truth:
    if not vis[i]:
        vis[i] = True
        Q.append(i)

while Q:
    cur = Q.popleft()

    for nxt in adj[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            Q.append(nxt)

rst = M - vis[100:].count(True)
print(rst)