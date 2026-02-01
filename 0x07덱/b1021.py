import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
idx = list(map(int, input().split()))
# 주어진 순서로 뽑아냄 

deq = deque()
cnt = 0
idxsort = sorted(idx)+[0]

for i in range(N):
    if i+1 == idxsort[cnt]:
        deq.append(i+1)
        cnt += 1
    else:
        deq.append(0)
# print(deq)

rst = 0
for i in idx:
    cnt = 0
    while i!=deq[0]:
        deq.rotate()
        cnt += 1
    rst += min(len(deq)-cnt, cnt)
    deq.popleft()

print(rst)