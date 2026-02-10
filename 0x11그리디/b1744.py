import sys
input = sys.stdin.readline

# a, b, c, d 순서로 클 때, ad+bc < ac+bd < ab+cd
# 재배열부등식과 같은 원리

N = int(input())
arr = [int(input()) for _ in range(N)]
rst = 0

arr.sort(reverse=True)
idx = 0
while idx<N:
    if arr[idx]>0:
        if idx<N-1 and arr[idx+1]>1:
            rst += arr[idx]*arr[idx+1]
            idx += 2
        else:
            rst += arr[idx]
            idx += 1
    else:
        break

arr.sort()
idx = 0
while idx<N:
    if arr[idx]<=0:
        if idx<N-1 and arr[idx+1]<=0:
            rst += arr[idx]*arr[idx+1]
            idx += 2
        else:
            rst += arr[idx]
            idx += 1
    else:
        break

print(rst)