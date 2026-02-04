import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().split())
ans = []

for c in combinations_with_replacement(range(1, N+1), M): # 중복조합
    ans.append(' '.join(map(str, c)))

print('\n'.join(ans))