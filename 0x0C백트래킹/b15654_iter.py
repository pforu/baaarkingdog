import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

for p in permutations(arr, M):
    ans.append(' '.join(map(str, p)))

print('\n'.join(ans))