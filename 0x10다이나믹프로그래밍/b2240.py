### 답 보고 구현 
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0] + [int(input()) for _ in range(T)]

d = [[0]*(W+1) for _ in range(T+1)]
# d[시간][이동횟수] = max(받은자두개수)

# 시간 흐르는 문제는 그냥 매 틱 돌리기 
# 시간이랑 이동횟수가 변수니까 그냥 2중for문 돌려서 각각 다 계산하면 됨 
for time in range(1, T+1): 
    for move in range(W+1):
        pos = 1 if move%2==0 else 2
        score = 1 if tree[time]==pos else 0
        if move==0:
            d[time][0] = d[time-1][0] + score
            # 이동 횟수가 0일때는 저번에서 이동해서 왔을 수가 없음 
        else:
            d[time][move] = max(d[time-1][move], d[time-1][move-1]) + score
            # 직전 틱에서 그대로 or 움직임 + 이번에 받았는지 

print(max(d[T]))