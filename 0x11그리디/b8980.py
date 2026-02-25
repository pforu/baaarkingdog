import sys
input = sys.stdin.readline
# import heapq
from collections import deque

N, C = map(int, input().split())
M = int(input())
info = [list(map(int, input().split())) for _ in range(M)]
info.sort(key=lambda x: x[1]) # 그리디의 핵심은 이 선택으로 발생하는 다른 경우의 손해를 최대한 줄이는 것 
# 따라서 정렬 기준이 빨리 끝나는 게 될 때가 많음 (회의실배정, 강의실배정, 멀티탭스케줄링)
# 점유 시간으로 기준을 착각하지 않도록 주의 

d = [0]*(N+1) # N인지 M인지 확실히 보기 
rst = 0
for box in info:
    st, en, wei = box
    mxwei = 0
    for i in range(st, en):
        if d[i] > mxwei:
            mxwei = d[i]
    # print(wei, mxwei)
    load = min(wei, C-mxwei)
    if load==0:
        continue
    rst += load
    for i in range(st, en):
        d[i] += load
# print(d)
print(rst)

# idx = 0
# box = 0
# truck = deque() # 스택 
# rst = 0
# for town in range(1, N+1): # 매 틱 검사 
#     print(town, truck)
#     while truck and truck[-1][0]==town: # 내리기 
#         thisbox = truck.pop()[1]
#         box -= thisbox
#         rst += thisbox
#         print(thisbox)
    
#     while idx<M and info[idx][0]==town: # 싣기 
#         if box + info[idx][2] <= C:
#             truck.append((info[idx][1], info[idx][2]))
#             box += info[idx][2]
#         elif box!=C:
#             truck.append((info[idx][1], C - box))
#             box = C
#         idx += 1

# print(rst)
            