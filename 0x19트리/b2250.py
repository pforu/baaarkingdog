import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())
pos = []

def inorder(cur, depth):
    if lc[cur]!=-1: inorder(lc[cur], depth+1)
    pos.append([depth, cur])
    if rc[cur]!=-1: inorder(rc[cur], depth+1)

lc = [-1]*(N+1)
rc = [-1]*(N+1)
not_root = [0]*(N+1)
for _ in range(N):
    n, l, r = map(int, input().split())
    lc[n] = l
    rc[n] = r
    if l!=-1: not_root[l] = 1 # 예외처리 항상 확실하게 
    if r!=-1: not_root[r] = 1

root = not_root[1:].index(0)
inorder(root+1, 1)
for i in range(N):
    pos[i][1] = i+1

pos.sort()
lvl_breadth = []
lvl = 1
min_pos = pos[0][1] # 초기값 설정 확실하게 
max_pos = pos[0][1]
for depth, num in pos:
    if lvl!=depth:
        lvl_breadth.append(max_pos - min_pos + 1)
        lvl += 1
        min_pos = num
    max_pos = num # 매 레벨의 첫 값도 설정해줘야 레벨에 노드가 하나일 때 전 레벨 값이 잘못 계산되지 않음 
lvl_breadth.append(max_pos - min_pos + 1) # 마지막은 무조건 안 들어감 

rst = [1, lvl_breadth[0]]
for lvl, breadth in enumerate(lvl_breadth):
    if breadth > rst[1]:
        rst = [lvl+1, breadth]
print(*rst)