import sys
input = sys.stdin.readline
# 최댓값 구하기 파라서치

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

def able(x, arr, N):
    cnt = 0
    for i in arr:
        cnt += i//x
    return cnt>=N

# 변수: 랜선길이 
l, r, ans = 1, 2**31-1, 0 # 최소값은 (1+1)//2=1, 최소최대 가능한 값 범위로 설정 
while l<=r:
    mid = (l+r)//2
    if able(mid, arr, N):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)