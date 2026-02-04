import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 사전 순으로 증가하는 순으로 ~ : sort 
ans = []

# 중복된 수 존재 가능 : set
for p in sorted(set(permutations(arr, M))): # set도 iterable, list로 감쌀 필요 X
    ans.append(' '.join(map(str, p)))
    
print('\n'.join(ans))

# 가로 중복 : before, set
# 세로 중복 : isused, st