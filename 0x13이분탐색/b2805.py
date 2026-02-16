import sys
input = sys.stdin.readline
# 최댓값 파라서치 
N, M = map(int, input().split())
tree = list(map(int, input().split()))

def able(x, tree, M):
    rst = 0
    for i in tree:
        rst += max(i-x, 0) # 식 주의해서 설정 
    return rst>=M # rst로 판단 (x가 아님)

l, r, ans = 0, 1000000000, 0 # 최소최대범위 설정 주의 
while l<=r:
    mid = (l+r)//2
    if able(mid, tree, M):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)