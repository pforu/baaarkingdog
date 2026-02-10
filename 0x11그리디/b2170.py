import sys
input = sys.stdin.readline
# 문제: 겹치는 걸 어떻게 파악할지
# 포함되면 겹치는 거, 끝점이 <=여야 포함, 연속된 수는 이어지지 않음 

# 비트마스킹은 좌표가 1억 이상이라 state의 메모리 초과 

# 배열 할당도 마찬가지의 문제 발생, 정렬하고 길이값, 부가정보만 가져가야 함 
# N=100만 이므로 NlogN까지 가능, 정렬하고 N으로 1회만 돌기 
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

s, e = arr[0][0], arr[0][1]-1
rst = 0
for val in arr:
    x, y = val[0], val[1]-1
    if x>e:
        rst += (e - s + 1)
        s, e = x, y
    elif y>e: # 아예 포함되면 갱신x
        e = y
rst += (e - s + 1)
print(rst)

# 비스마스킹 
# N = int(input())
# state = 0
# for _ in range(N):
#     s, e = map(int, input().split())
#     mask = ((1 << (e - s)) - 1) << s
#     state |= mask
# print(state.bit_count())