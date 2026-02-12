import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
ans = []

for _ in range(N):
    inp = int(input())
    if inp==0:
        ans.append(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, inp)

print('\n'.join(map(str, ans)))