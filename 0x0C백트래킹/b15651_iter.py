import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().split())
ans = []

for p in product(range(1, N+1), repeat=M): # 중복순열 
    ans.append(' '.join(map(str, p)))

print('\n'.join(ans))