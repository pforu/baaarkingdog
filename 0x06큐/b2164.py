import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()
for i in range(N):
    queue.append(i+1)
for _ in range(N-1):
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)