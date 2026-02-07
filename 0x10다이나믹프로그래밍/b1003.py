import sys
input = sys.stdin.readline
# 피보나치의 성질 그대로 이용 

T = int(input())
d = [[1, 0], [0, 1]] + [[0, 0] for _ in range(40)]
for i in range(2, 41):
    for j in range(2):
        d[i][j] = d[i-1][j] + d[i-2][j]
ans = []
for i in range(T):
    n = int(input())
    ans.append(d[n])
print('\n'.join(f"{row[0]} {row[1]}" for row in ans))