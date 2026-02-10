###### 잘못된 코드 ######
# 현재 범위 안에서 어떤 꽃이 가장 멀리 가는지를 확정하지 못함
# 연속성이 보장되지 않음 


import sys
input = sys.stdin.readline

# 3월 1일부터 11월 30일까지
# 스케쥴링이랑 비슷
# 겹치는 일수 최소, 비는 날 불가 
# 10만이라 상태 반영하는 dp 불가
# 정렬은 해야 함
# 기준은 길면 좋음, 기준이 시작하는 날이 빠른 거, 끝나는 날 느린 거

N = int(input())
arr = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    arr.append((100*a + b, 100*c + d))

arr.sort(key=lambda x: (x[0], -x[1])) 
rst = 0
last = 0
val = arr[0]
found = False
i = 0
print(arr)
while i<N:
    x = arr[i]
    if x[1]<=301:
        continue
    if x[0]>1130:
        found = True
        break
    if x[0]>last: # 넘어감
        print(x)
        last = val[1]
        rst += 1
        i -= 1
    val = x
    i += 1
if not found:
    rst += 1
print(rst)