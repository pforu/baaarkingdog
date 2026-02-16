import sys
input = sys.stdin.readline
# 최솟값 파라서치 FFFTTTT

N, M, L = map(int, input().split())
coor = [0] + list(map(int, input().split())) + [L] # 1 ≤ 휴게소의 위치 ≤ L-1
coor.sort()

def able(x, coor, M): # 최대 거리를 x로 유지할 때 몇 개만 설치해도 되는지 
    cnt = 0
    for b, n in zip(coor[:-1], coor[1:]):
        diff = n - b
        cnt += (diff-1)//x
    return cnt<=M


# 변수: 휴게소 간 최대 거리 
l, r, ans = 1, L-1, 0
while l<=r:
    mid = (l+r)//2
    if able(mid, coor, M): # 덜 설치해도 거리 mid는 됨 
        ans = mid
        r = mid - 1 # 최대거리 더 좁혀도 이만큼 설치해서 되나? 
    else:
        l = mid + 1
print(ans)    