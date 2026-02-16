### AC
import sys
input = sys.stdin.readline
# 최솟값 파라서치

N, M, L = map(int, input().split())
coor = [0] + list(map(int, input().split())) + [L]
coor.sort()

def able(x, coor, M):
    cnt = 0
    idx = 0
    bef = 0
    while idx<len(coor):
        if bef+x<coor[idx]:
            cnt += 1
            bef += x
        else:
            bef = coor[idx]
            idx += 1
    return cnt<=M


# 변수: 휴게소 간 최대 거리 
l, r, ans = 1, L, 0
while l<=r:
    mid = (l+r)//2
    if able(mid, coor, M):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)    