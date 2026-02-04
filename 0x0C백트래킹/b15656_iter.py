import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

for p in product(arr, repeat=M):
    ans.append(' '.join(map(str, p)))
    
print('\n'.join(ans))