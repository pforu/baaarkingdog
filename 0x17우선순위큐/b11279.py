import sys
input = sys.stdin.readline
import heapq

N = int(input())
h = []
ans = []
for i in range(N):
    inp = int(input())
    if inp==0:
        ans.append(-heapq.heappop(h)) if h else ans.append(0)
    else:
        heapq.heappush(h, -inp)
print("\n".join(map(str, ans)))
