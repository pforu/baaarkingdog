import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.extend(list(map(int, input().split())))
cctv = []
wall = []
for idx in range(N*M):
    cur = board[idx]
    match cur:
        case 6:
            wall.append(idx)
        case 0:
            continue
        case default:
            cctv.append((idx, cur))

vis = board.copy()

def go(x, y, cur, to, til):
    nxt_idx = [x, y]
    step = 0
    while 0<=nxt_idx[cur]<til and board[nxt_idx[0]*M+nxt_idx[1]]!=6:
        if board[nxt_idx[0]*M+nxt_idx[1]]<=0:
            vis[nxt_idx[0]*M+nxt_idx[1]] -= 1
        nxt_idx[cur] += to
        step += 1
    return (nxt_idx, cur, to, step)

def rev_go(idx, cur, to, step):
    rev_idx = idx.copy()
    for _ in range(step):
        rev_idx[cur] -= to
        if board[rev_idx[0]*M+rev_idx[1]]<=0:
            vis[rev_idx[0]*M+rev_idx[1]] += 1

rst = 64

def func(idx):
    if idx==len(cctv):
        global rst
        rst = min(rst, vis.count(0))
        # if rst==10:
        #     print(*vis)
        return
    
    pos, num = cctv[idx][0], cctv[idx][1]
    cx, cy = pos//M, pos%M

    if num==1:
        for cur, to, til in [(0, 1, N), (0, -1, N), (1, 1, M), (1, -1, M)]:
            rev_idx, rev_cur, rev_to, rev_step = go(cx, cy, cur, to, til)
            func(idx+1)
            rev_go(rev_idx, rev_cur, rev_to, rev_step)

    elif num==2:
        for cur, til in [(0, N), (1, M)]:
            rev_info = []
            for to in [-1, 1]:
                rev_info.append(go(cx, cy, cur, to, til))
            func(idx+1)
            for rev_idx, rev_cur, rev_to, rev_step in rev_info:
                rev_go(rev_idx, rev_cur, rev_to, rev_step)
    
    elif num==3:
        for cur, to, til in [(0, 1, N), (0, -1, N)]:
            for cur2, to2, til2 in [(1, 1, M), (1, -1, M)]:
                rev_info = []
                rev_info.append(go(cx, cy, cur, to, til))
                rev_info.append(go(cx, cy, cur2, to2, til2))
                func(idx+1)
                for rev_idx, rev_cur, rev_to, rev_step in rev_info:
                    rev_go(rev_idx, rev_cur, rev_to, rev_step)

    elif num==4:
        for i in range(4):
            rev_info = []
            for j, (cur, to, til) in enumerate([(0, 1, N), (0, -1, N), (1, 1, M), (1, -1, M)]):
                if i!=j:
                    rev_info.append(go(cx, cy, cur, to, til))
            func(idx+1)
            for rev_idx, rev_cur, rev_to, rev_step in rev_info:
                rev_go(rev_idx, rev_cur, rev_to, rev_step)
    
    elif num==5:
        rev_info = []
        for cur, to, til in [(0, 1, N), (0, -1, N), (1, 1, M), (1, -1, M)]:
            rev_info.append(go(cx, cy, cur, to, til))
        func(idx+1)
        for rev_idx, rev_cur, rev_to, rev_step in rev_info:
            rev_go(rev_idx, rev_cur, rev_to, rev_step)
    

func(0)
print(rst)