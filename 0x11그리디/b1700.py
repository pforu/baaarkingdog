###### 잘못된 코드 ######
# 전체적으로 짧게 쓰는 게 아니라, 현재 기준 가장 나중에 쓸 걸 빼는 거

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))

ord_s = [-1]*K
ord_e = [-1]*K
for i, val in enumerate(order):
    if ord_s[val-1]==-1:
        ord_s[val-1] = i
for i, val in enumerate(order[::-1]):
    if ord_e[val-1]==-1:
        ord_e[val-1] = K-i+1
ord_len = [0]*K
for i, val in enumerate(zip(ord_s, ord_e)):
    ord_len[i] = (val[1]-val[0]+1, val[0], val[1])

cur = [-1]*K
cur_cnt = 0
rst = 0
for time, val in enumerate(order):
    if cur[val-1]!=-1:
        continue
    if cur_cnt>=N:
        min_idx = 0
        for i, cnt in enumerate(cur):
            if cnt!=-1 and cnt<cur[min_idx]:
                min_idx = i
        cur[min_idx] = -1
        cur_cnt -= 1
        rst += 1
    cur[val-1] = ord_len[val-1][0]
    cur_cnt += 1

    # for num, end in enumerate(ord_len):
    #     if end[2]<=time:
    #         cur[num] = -1
    #         cur_cnt -= 1

print(rst)
