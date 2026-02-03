import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, n + 1)]
ans = []

# permutations를 이용해 M개를 뽑는 순열 생성
for p in permutations(numbers, m):
    ans.append(' '.join(map(str, p)))

print('\n'.join(ans))