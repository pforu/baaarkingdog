import sys
input = sys.stdin.readline
import heapq

T = int(input())
ans = []
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    h = []
    for a in arr:
        heapq.heappush(h, a)
    rst = 0
    while len(h)>1:
        a, b = heapq.heappop(h), heapq.heappop(h)
        rst += (a+b)
        heapq.heappush(h, a+b)
    ans.append(rst)
print('\n'.join(map(str, ans)))