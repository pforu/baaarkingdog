import sys
input = sys.stdin.readline
# 맨 왼쪽 위 구석의 타일을 각 모양의 타일이 점유하면 어떻게 되는지 생각 

N = int(input())
d = [0, 1, 3] + [0]*N
for i in range(3, N+1):
    d[i] = (2*d[i-2] + d[i-1]) % 10007
print(d[N])