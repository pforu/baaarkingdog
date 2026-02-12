import sys
input = sys.stdin.readline
import heapq
# 그리디: 합친 쪽이 더 많이 비교당할 것이기 때문
# 허프만 코딩과 알고리즘 동일

N = int(input())
heap = [int(input()) for _ in range(N)]
heapq.heapify(heap)

rst = 0

while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    rst += (a+b)
    heapq.heappush(heap, a+b)

print(rst)