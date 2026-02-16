import sys
input = sys.stdin.readline
# 최댓값 파라서치 TTTFFFF

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

def able(x, house, C):
    rst = 0
    bef = house[0]
    for i in house:
        if i-bef>=x:
            rst += 1
            bef = i
    return rst>=C
    

# 변수: 공유기 간 최소 거리 
l, r, ans = 1, 1000000000, 0 # 거리를 변수로 잡았으므로 좌표범위(l=0) 넣으면 안 됨
while l<=r:
    mid = (l+r)//2
    if able(mid, house, C-1):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)