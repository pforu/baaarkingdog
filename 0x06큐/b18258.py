import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()

for i in range(N):
    ins = input().split()
    match ins[0]:
        case "push":
            queue.append(ins[1])
        case "pop":
            print(queue.popleft() if queue else -1)
        case "size":
            print(len(queue))
        case "empty":
            print(0 if queue else 1) ### 언제 0/1인지 주의 
        case "front":
            print(queue[0] if queue else -1)
        case "back":
            print(queue[-1] if queue else -1)