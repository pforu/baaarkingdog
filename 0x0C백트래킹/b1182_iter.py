import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    for c in combinations(arr, i): # 풀리지만, 조합을 다 생성하고 합을 매번 구해서 효율 저하
        if sum(c)==M:
            cnt += 1

print(cnt)