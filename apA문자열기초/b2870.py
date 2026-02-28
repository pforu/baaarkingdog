import sys
input = sys.stdin.readline
import re

N = int(input())
nums = []
for _ in range(N):
    inp = input().strip()
    nums.extend(re.findall(r'\d+', inp))
print(*sorted(list(map(int, nums))), sep='\n')