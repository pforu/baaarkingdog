import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 사전 순으로 증가하는 순으로 ~ : sort 
ans = []

# # 고른 수열은 비내림차순, 같은 수를 여러 번 골라도 된다 : 중복조합 
for c in combinations_with_replacement(arr, M):
    ans.append(' '.join(map(str, c)))
    
print('\n'.join(ans))