import sys
input = sys.stdin.readline
from collections import deque
# 파이썬은 딕셔너리가 더 낫긴 함

rst = [[], [], []]

def preorder(cur):
    rst[0].append(cur)
    if lc[cur]: preorder(lc[cur])
    if rc[cur]: preorder(rc[cur])

def inorder(cur):
    if lc[cur]: inorder(lc[cur])
    rst[1].append(cur)
    if rc[cur]: inorder(rc[cur])

def postorder(cur):
    if lc[cur]: postorder(lc[cur])
    if rc[cur]: postorder(rc[cur])
    rst[2].append(cur)

N = int(input())
lc = [0]*(N+1)
rc = [0]*(N+1)
for _ in range(N):
    n, l, r = input().split()
    lc[ord(n)-ord('A')+1] = (ord(l)-ord('A')+1 if l!='.' else 0)
    rc[ord(n)-ord('A')+1] = (ord(r)-ord('A')+1 if r!='.' else 0)

preorder(1)
inorder(1)
postorder(1)

for i in range(3):
    ans = []
    for val in rst[i]:
        ans.append(chr(val+ord('A')-1))
    print(''.join(ans))