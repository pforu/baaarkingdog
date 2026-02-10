import sys
input = sys.stdin.readline
# Belady’s Algorithm - Optimal Page Replacement
# 현재 내가 가진 데이터 중 가장 효율이 떨어지는 요소를 골라낸다

N, K = map(int, input().split())
devices = list(map(int, input().split()))

rst = 0
plugs = set()

for i, device in enumerate(devices):
    if device in plugs:
        continue

    if len(plugs)>=N:
        nxt_use = {x:K for x in plugs}
        for j, val in enumerate(devices[i+1:]):
            if val in plugs and nxt_use[val]==K:
                nxt_use[val] = j
        max_key = -1
        for val, nxt in nxt_use.items():
            if max_key==-1 or nxt>nxt_use[max_key]:
                max_key = val
        plugs.remove(max_key)
        rst += 1
    plugs.add(device)

print(rst)