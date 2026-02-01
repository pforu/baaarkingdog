import sys
input = sys.stdin.readline
from collections import deque

# 움직이는 조건이 while Q가 아니라는 거 - 무조건 답을 찾을 수 있으니까 
# 탐색을 DIRS에서 하는 게 아니라 문제 조건에 따라 -1, +1, *2로 한다는 거 

N, K = map(int, input().split())

dist = [-1]*100005
Q = deque()

dist[N] = 0
Q.append(N)

while dist[K]==-1:
    cur = Q.popleft()
    for nxt in [cur-1, cur+1, cur*2]:
        if 0 <= nxt <= 100000 and dist[nxt]==-1:
            # 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다
            dist[nxt] = dist[cur] + 1
            Q.append(nxt)

print(dist[K])