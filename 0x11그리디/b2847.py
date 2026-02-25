import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.reverse()

bef = arr[0]+1
cnt = 0
for val in arr:
    d = max(val-bef+1, 0)
    cnt += d
    bef = val-d
print(cnt)