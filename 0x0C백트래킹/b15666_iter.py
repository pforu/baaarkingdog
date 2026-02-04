import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
ans = []

for c in sorted(combinations_with_replacement(arr, M)): 
    ans.append(' '.join(map(str, c)))
    
print('\n'.join(ans))
