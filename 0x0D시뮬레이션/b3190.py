import sys
input = sys.stdin.readline
from collections import deque
### 맨 위 맨 좌측 (1행 1열) : 문제 정말 꼼꼼히 읽기..

N = int(input())
K = int(input())
apple = set([tuple(map(int, input().split())) for _ in range(K)])
L = int(input())
info = [list(input().split()) for _ in range(L)]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우하좌상 순, D일 때 +1, L일 때 -1

snakeset = set([(1, 1)])
snake = deque([(1, 1)])
head, tail = (1, 1), (1, 1)
dir = 0
idx = 0
time = 0
while True:
    # print(head)
    time += 1

    head = (head[0]+DIRS[dir][0], head[1]+DIRS[dir][1]) # 1

    if not (0<head[0]<=N and 0<head[1]<=N) or head in snakeset: # 2
        break
    snakeset.add(head)
    snake.appendleft(head)

    if head in apple: # 3
        apple.remove(head)

    else: # 4
        snakeset.remove(tail)
        snake.pop()
        tail = snake[-1]
    
    if idx<L and time==int(info[idx][0]): # 방향전환 
        dir = dir - 1 if info[idx][1]=='L' else dir + 1
        dir %= 4
        idx += 1

print(time)