import sys
input = sys.stdin.readline

T = int(input())
arr = [int(input()) for _ in range(T)]
# N<=1,000,000

d = [0, 1, 2, 4]
for i in range(4, 1000003):
    d.append((d[i-1] + d[i-2] + d[i-3]) % 1000000009)
ans = []
for n in arr:
    ans.append(d[n])
print('\n'.join(map(str, ans)))