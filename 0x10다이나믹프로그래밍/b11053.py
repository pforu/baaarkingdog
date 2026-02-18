import sys
input = sys.stdin.readline
# d를 돌면서 arr[i]>arr[j]인데 그 중 d[j]가 가장 큰 걸 고름
# d[i]가 꼭 d[i-1] 등 주변 항으로만 연속되게 정의될 필요 없음

N = int(input())
arr = [0] + list(map(int, input().split()))
d = [0] + [0]*N

for i in range(1, N+1):
    d[i] = 1 # 못 찾으면 걔부터 부분수열 시작 
    for j in range(1, i):
        if arr[i]>arr[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))



# 이분탐색의 nlogn 코드 존재
# from bisect import bisect_left

# N = int(input())
# arr = list(map(int, input().split()))

# stack = [arr[0]]

# for i in range(1, N):
#     if arr[i] > stack[-1]: 
#         stack.append(arr[i]) # 크면 그냥 붙이기 
#     else:
#         # stack 안에서 arr[i]가 들어갈 자리를 이분 탐색으로 찾음
#         idx = bisect_left(stack, arr[i])
#         stack[idx] = arr[i] # 덮어씌우기
#         # 결국 더 작은 수로 덮어씌워짐, 가능성이 무조건 늘어남 

# print(len(stack))