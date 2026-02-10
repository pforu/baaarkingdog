import sys
input = sys.stdin.readline
# 그리디: 지금 피어있는 것 중에 제일 나중에 지는 것 선택 
# 최선의 선택(지금 피어 있으면서 가장 오래 가는 것)은 덜 좋은 선택의 기간을 반드시 포함함 
# 그 다음 꽃을 고를 때는 다시 모든 걸 보게 

N = int(input())
arr = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    arr.append((100*a + b, 100*c + d))

t = 301 # 현재 시간
rst = 0
while t<=1130:
    nxt_t = t
    for x in arr:
        if x[0]<=t and x[1]>nxt_t: # 더 나중에 지는 걸 발견하면 갱신 
            nxt_t = x[1]
    if nxt_t==t: # 조건에 맞는 게 없었음 
        rst = 0
        break
    rst += 1
    t = nxt_t # 현재 시간을 지는 때로 옮기기 
print(rst)