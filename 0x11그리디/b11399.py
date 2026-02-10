import sys
input = sys.stdin.readline

# 그리디인 이유: N명일 경우, 1번시간*N + 2번시간*N-1 + .. 이므로 정렬해서 최소순으로 세우기

N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
rst = 0
for i, val in enumerate(arr):
    rst += (i+1)*val
print(rst)