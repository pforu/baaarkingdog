import sys
input = sys.stdin.readline
import heapq
# 스케쥴링 그리디에서 기준을 모르겠으면 반대로 거슬러오기 

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

idx = N-1
rst = 0
heap = []
for i in range(N, 0, -1):
    while idx>=0 and arr[idx][0]>=i:
        heapq.heappush(heap, (-arr[idx][1], -arr[idx][0]))
        idx -= 1
    # while heap and -heap[0][1]>i: # 뒤에서 오니까 넘었어도 후보에서 빼면 안 됨 
    #     heapq.heappop(heap)
    if heap:
        rst += -heapq.heappop(heap)[0]
    # if idx==-1: # 힙에 후보들이 존재, 끝내면 안 됨
    #     break

print(rst)

# 컵라면 수 기준 정렬의 반례
# 4
# 4 100
# 1 2
# 2 3
# 3 4