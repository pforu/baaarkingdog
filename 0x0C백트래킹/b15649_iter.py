import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, n + 1)]
ans = []

for p in permutations(numbers, m): # 순열 
    ans.append(' '.join(map(str, p)))

print('\n'.join(ans))