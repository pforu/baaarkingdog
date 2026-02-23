### 정렬하고 한 번만 도는 풀이 


import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    arr.append((100*a + b, 100*c + d))

# 1. 시작일 기준 정렬 (O(N log N))
arr.sort()

t = 301
rst = 0
idx = 0
found_total = False

while t <= 1130:
    nxt_t = t
    found_flower = False
    
    # 2. 현재 시간(t) 이전에 시작하는 꽃들 중 가장 늦게 지는 꽃 찾기
    # idx를 초기화하지 않고 계속 이어서 가기 때문에 O(N)
    while idx < N: # 가능한 후보군 중 가장 늦게 지는 걸로 갱신 
        if arr[idx][0] <= t:
            if arr[idx][1] > nxt_t:
                nxt_t = arr[idx][1]
                found_flower = True
            idx += 1
        else:
            # 시작일이 t보다 뒤에 있으면 더 이상 볼 필요 없음 (정렬 덕분)
            break
            
    if not found_flower: # 못 찾으면 그대로 끝, found_total이 True가 되지 못함 
        break
    
    rst += 1
    t = nxt_t
    
    if t > 1130:
        found_total = True
        break

print(rst if found_total else 0)