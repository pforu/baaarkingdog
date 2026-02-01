import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
stack = deque()
for _ in range(K):
    n = int(input())
    stack.append(n) if n!=0 else stack.pop()
print(sum(stack))