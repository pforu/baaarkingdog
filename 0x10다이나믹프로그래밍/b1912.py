import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

d = [-1003] + [0]*N ### i번째항까지의 수열의 최대 
for i in range(1, N+1): # N+1 좀 신경써 제발 
    d[i] = max(d[i-1] + arr[i], arr[i])
print(max(d))

# pfs = [0]*(N+1) # 누적합 
# for i in range(1, N+1):
#     pfs[i] = pfs[i-1] + arr[i]

# rst = arr[1]
# for i in range(1, N+1): # 다 돌릴 필요 없음, 최댓값은 유일 
#     for j in range(i, N+1): # 투포인터적으로 생각해보기 
#         rst = max(rst, pfs[j]-pfs[i-1])
# print(rst)