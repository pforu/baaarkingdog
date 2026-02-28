import sys
input = sys.stdin.readline
import math

mes = input().strip()
n = len(mes)
r, c = 0, 0
for i in range(int(math.sqrt(n)), 0, -1):
    if n/i == n//i:
        r, c = i, n//i
        break

ans = []
for i in range(r):
    for j in range(c):
        ans.append(mes[r*j+i])
print(''.join(ans))