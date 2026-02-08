import sys
input = sys.stdin.readline
from collections import deque
# N극은 0, S극은 1
# 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
# 오른쪽은 2번(rotate(-1)*2의 q[0]), 왼쪽은 6번 톱니(rotate(1)*2의 q[0]), 전체 8개(0~7)

wheel = [deque(map(int, input().strip())) for _ in range(4)]

def pole(): # 각 바퀴의 왼/오 확인 
    poles = []
    for i in range(4):
        w = wheel[i]
        for j in (1, -1): # 오른쪽, 왼쪽으로 각각 2번씩 돌리고 첫 값 확인 
            w.rotate(2*j)
            poles.append(w[0])
            w.rotate(-2*j)
    return poles

def rotate(poles, num, dir):
    dirs = [] # 상대적 방향(같으면 0, 다르면 -1, 본인은 1), 계수 
    for i in range(1, 6, 2):
        dirs.append(0 if poles[i]==poles[i+1] else -1) # 바퀴 만나는 곳에서 극 같은지 확인 
    dirs.insert(num-1, 1) # 본인 넣기 

    for i in (1, -1): #확산
        idx = num-1
        d = dir
        while 0<=idx<4:
            if d==0: # 같은 극 나온 순간부터 그 다음 것들도 더 이상 안 돌아감 
                break
            wheel[idx].rotate(d*dirs[idx]) # 직전 바퀴방향에 상대적 방향 곱해 돌리기 
            d *= dirs[idx] # 이번 바퀴방향 저장 
            idx += i
    wheel[num-1].rotate(-dir) # 본인 2번 돌아간 거 보정 

            

T = int(input())
for i in range(T):
    num, dir = map(int, input().split())
    rotate(pole(), num, dir)

rst = 0
for i in range(4):
    rst += wheel[i][0] * (2**i)
print(rst)