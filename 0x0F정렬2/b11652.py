import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]+[float('inf')]

# 카운트 배열을 쓸 수 없을 정도의 수의 범위라면
# 정렬하면 같은 수끼리 인접한다는 성질 사용
arr.sort()

cnt = 1
before = arr[0]
maxcnt = -1
maxint = float('-inf')
for i in range(1, N+1):
    if arr[i]==before:
        cnt += 1
    else:
        if cnt>maxcnt:
            maxcnt = cnt
            maxint = before
        cnt = 1
    before = arr[i]

print(maxint)