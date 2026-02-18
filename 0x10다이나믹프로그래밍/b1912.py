import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

d = [-1003] + [0]*N ### i번째항까지의 수열의 최대 
for i in range(1, N+1): # N+1 좀 신경써 제발 
    d[i] = max(d[i-1] + arr[i], arr[i])
    # current_max = max(current_max + arr[i], arr[i])
    # d 전체 유지할 필요 없음 
print(max(d))

# 이전까지 더해온 값에 현재 값을 더하는 게 이득인가,
# 아니면 지금부터 새로 시작하는 게 이득인가?

# pfs = [0]*(N+1) # 누적합 
# for i in range(1, N+1):
#     pfs[i] = pfs[i-1] + arr[i]

# rst = arr[1]
# for i in range(1, N+1): # 다 돌릴 필요 없음, 최댓값은 유일 
#     for j in range(i, N+1): # 투포인터적으로 생각해보기 
#         rst = max(rst, pfs[j]-pfs[i-1])
# print(rst)