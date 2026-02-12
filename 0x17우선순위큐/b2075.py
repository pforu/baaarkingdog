import sys
input = sys.stdin.readline
import heapq
# 정렬의 경우 전체를 다 봐야 돼서 확정 Nlogn이지만,
# 힙은 k번째 큰 수만 요구할 경우 자체 크기를 k로 유지해서 시간복잡도 줄일 수 있음

N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N-1):
    inp = map(int, input().split())
    for val in inp:
        if val>heap[0]: # 필요할 때만 push/pop 수행, lgN이라 꽤 잡아먹음 
            heapq.heappush(heap, val)
            heapq.heappop(heap)

# N = int(input())
# heap = []
# for _ in range(N):
#     inp = map(int, input().split())
#     for val in inp:
#         heapq.heappush(heap, val)
#         if len(heap)>N:
#             heapq.heappop(heap)
# N * N * 2lgN

print(heap[0])