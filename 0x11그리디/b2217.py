import sys
input = sys.stdin.readline

# 1. 완탐: 1~N개의 모든 조합 시도
# 2. DP: d[i][k][min] = i번째까지 고려했을 때 k개를 골랐고
# 그중 최솟값은 min (정렬로 최솟값정보&i 뺄 수 있게 됨) - 완탐과 다를 게x
# 3. 그리디: 고를 거면 최대중량 큰 걸 고르는 게 최선

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort(reverse=True)
rst = 0
for i in range(N):
    rst = max(rst, arr[i]*(i+1))
print(rst)