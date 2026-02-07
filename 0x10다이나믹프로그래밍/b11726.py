import sys
input = sys.stdin.readline

N = int(input())
d = [0, 1, 2] + [0]*N
for i in range(3, N+1): # N까지 포함시키기 
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[N])