### 나중에 다시 하기 

import sys
input = sys.stdin.readline

N = int(input())
d = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, i):
        d[i] = max(d[i], d[i-j] + d[j])

print(d[N])