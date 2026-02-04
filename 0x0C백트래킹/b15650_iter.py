import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)] 
ans = []

for c in combinations(arr, M): # 조합 
    ans.append(' '.join(map(str, c)))

print('\n'.join(ans))

# 참고용: 이런 문법도 가능~ (제너레이터 사용으로 메모리 아낌)
# print('\n'.join(' '.join(map(str, c)) for c in combinations(range(1, N+1), M)))