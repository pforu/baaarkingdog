import sys
input = sys.stdin.readline

N = int(input())
d = [0, 1, 1]
for i in range(3, N+1):
    d.append(d[i-1] + d[i-2])
print(d[-1])