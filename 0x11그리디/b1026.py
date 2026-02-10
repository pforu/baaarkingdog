import sys
input = sys.stdin.readline

# 1. 완탐: N!
# 2. DP: d[i][state] A의 i번째까지 결정했고, B에서 뭘 사용했는지 정보 필요 
# 3. 그리디: 재배열 부등식

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

rst = 0
for i in range(N):
    rst += a[i]*b[i]
print(rst)