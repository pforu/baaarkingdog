import sys
input = sys.stdin.readline
# 이번 단계에서 
# 0으로 끝나는 이친수는 직전 이친수의 끝에 0을 붙인 것
# 1로 끝나는 이친수는 직전 이친수 중 0으로 끝나는 것에 1을 붙인 것 
# 토끼 성장이랑 비슷한 듯 

N = int(input())
d = [[0, 0], [0, 1]] + [[0]*2 for _ in range(N)]
for i in range(2, N+1):
    d[i][0] = d[i-1][0] + d[i-1][1]
    d[i][1] = d[i-1][0]

print(sum(d[N]))