import sys
input = sys.stdin.readline

# 1. 완탐: 모든 조합 보고(선택/미선택이므로 2**N) 안 겹치는지 확인해서 최댓값 갱신 
# 2. DP: d[i] = i시간에 끝나는 회의의 최댓값 (like 퇴사)
# 3. 그리디: (상담길이와 별개로 가치가 정해져 있는 퇴사 문제와 달리) 빨리 끝나고, 짧을수록 최선 

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))
last = -1
rst = 0
for x in arr:
    if last<=x[0]:
        last = x[1]
        rst += 1
print(rst)