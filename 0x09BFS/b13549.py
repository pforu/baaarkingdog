import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAX = 200003
dist = [-1] * MAX # dist[좌표] = 시간 

Q = deque()
dist[N] = 0
Q.append(N)

# 간선의 비용이 동일할 때 : 일반 BFS (queue)
# 간선의 비용이 0/1일 때 : 0-1 BFS (deque - appendleft/append)
# 간선의 비용이 다양할 떄(음수 없음) : 다익스트라 (heapq)
# 음수 간선이 있을 때 : 벨만-포드 / 플로이드-워셜 

# 0-1 BFS는 큐에 넣을 때 최단 거리가 확정됨 
# dist[cur]+time < dist[pos]는 다익스트라에 가까움
# 동작은 하지만 dist[pos]==-1만 확인해도 충분 
while Q:
    cur = Q.popleft()
    if cur==K:
        break

    for pos in [cur*2]: # teleport 
        if 0<=pos<MAX and (dist[pos]==-1 or dist[cur] < dist[pos]):
            #print(pos)
            dist[pos] = dist[cur]
            Q.appendleft(pos)

    for pos in [cur+1, cur-1]: # walk
        if 0<=pos<MAX and (dist[pos]==-1 or dist[cur]+1 < dist[pos]):
            #print(pos)
            dist[pos] = dist[cur] + 1
            Q.append(pos)

print(dist[K])            