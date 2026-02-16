import sys
input = sys.stdin.readline
import bisect

N = int(input())
sol = list(map(int, input().split()))
# 서로 다른 용액을 혼합

ans = int(1e11)
sols = [0, 0]
for i, val in enumerate(sol):
    idx = bisect.bisect_left(sol, -val)
    for j in range(idx-1, idx+2):
        if j<0 or j>=N or i==j: continue
        if abs(val + sol[j]) < ans:
            ans = abs(val + sol[j]) # 여기도 abs 해야 됨, 합 자체는 중요하지 않고 비교에만 쓰니까 
            sols = [val, sol[j]]

print(*sorted(sols))