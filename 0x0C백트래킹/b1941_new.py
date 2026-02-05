import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

board = [input().strip() for _ in range(5)]
flat_board = "".join(board)

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def search(comb):
    dasom = 0
    for idx in comb:
        if flat_board[idx] == 'S':
            dasom += 1
    if dasom < 4: 
        return False

    # 2. 연결성 체크 (BFS)
    # nodes: 이번 조합에 포함된 인덱스들의 집합
    nodes = set(comb)
    start_node = comb[0]
    q = deque([start_node])
    vis = {start_node}
    
    while q:
        curr = q.popleft()
        
        # 1차원 인덱스를 2차원 좌표로 변환
        cx, cy = curr // 5, curr % 5
        
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                n_idx = nx * 5 + ny
                # 명단(nodes)에 있고, 아직 안 가본(vis) 곳이라면
                if n_idx in nodes and n_idx not in vis:
                    vis.add(n_idx)
                    q.append(n_idx)
    
    # 3. 7개가 모두 연결되었는지 확인
    return len(vis) == 7

# 전체 조합 탐색
rst = 0
for c in combinations(range(25), 7):
    if search(c):
        rst += 1

print(rst)