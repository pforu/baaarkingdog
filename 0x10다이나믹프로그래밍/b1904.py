import sys
input = sys.stdin.readline

N = int(input())
d = [0, 1, 2] + [0]*N
for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2]) % 15746
print(d[N]%15746)