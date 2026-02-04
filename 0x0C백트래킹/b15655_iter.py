import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

for c in combinations(arr, M):
    ans.append(' '.join(map(str, c)))
    
print('\n'.join(ans))