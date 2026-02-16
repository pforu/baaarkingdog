import sys
input = sys.stdin.readline
import bisect

N = int(input())
coor = list(map(int, input().split()))
uni = sorted(list(set(coor)))

ans = []
for i in coor:
    ans.append(bisect.bisect_left(uni, i))
print(*ans)