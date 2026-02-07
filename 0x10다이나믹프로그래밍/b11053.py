import sys
input = sys.stdin.readline
# d를 돌면서 arr[i]>arr[j]인데 그 중 d[j]가 가장 큰 걸 고름
# d[i]가 꼭 d[i-1] 등 주변 항으로만 연속되게 정의될 필요 없음

N = int(input())
arr = [0] + list(map(int, input().split()))
d = [0] + [0]*N

for i in range(1, N+1):
    d[i] = 1 # 못 찾으면 걔부터 부분수열 시작 
    for j in range(1, i):
        if arr[i]>arr[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))