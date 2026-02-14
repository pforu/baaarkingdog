import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]
DIRS = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
d = dict() # 주어진 수 범위 보고 미리 저장해놓는 것 떠올리기 (K=1000)
Q = deque()

for i in range(N):
    for j in range(M):
        len1 = board[i][j]
        Q.append((i, j, len1))
        d[len1] = d[len1] + 1 if len1 in d else 1 # 0 아니고 1임 

        while Q:
            cx, cy, word = Q.popleft()
            if len(word)>=5: # 여기서 처리 
                continue
            for dx, dy in DIRS:
                nx, ny = (cx + dx) % N, (cy + dy) % M # %로 격자 안에 두는 기믹 꼭 기억 
                cur_word = word + board[nx][ny]
                d[cur_word] = d[cur_word] + 1 if cur_word in d else 1
                Q.append((nx, ny, cur_word))

ans = []
for i in range(K):
    val = input().strip()
    ans.append(d[val] if val in d else 0)
print('\n'.join(map(str, ans)))