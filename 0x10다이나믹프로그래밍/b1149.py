import sys
input = sys.stdin.readline

N = int(input())
arr = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
d = [arr[0], arr[1]] + [[0]*3 for _ in range(N)]

for i in range(2, N+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + arr[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + arr[i][1]
    d[i][2] = min(d[i-1][1], d[i-1][0]) + arr[i][2]

print(min(d[N]))