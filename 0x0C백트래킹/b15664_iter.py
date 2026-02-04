import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) 
ans = []

# 결과적으로 중복이 나오는 걸 피해야 된다면 (중복 수를 없애는 게 아님)
for p in sorted(set(combinations(arr, M))):
    ans.append(' '.join(map(str, p)))
    
print('\n'.join(ans))
