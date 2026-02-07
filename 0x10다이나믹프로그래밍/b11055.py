import sys
input = sys.stdin.readline
# d[i] : i번째 항으로 끝나는, 가장 큰 증가수열의 값 

N = int(input())
arr = [0] + list(map(int, input().split()))

d = [0] + [0]*N
for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        if arr[j]<arr[i]:
            d[i] = max(d[i], d[j] + arr[i])
            # break이 아니라, 다 보면서 d[j]가 제일 큰 걸 찾아야 함 
print(max(d))

# 증가 수열 = 단조 증가
# 증가가 끊기면 : 그 수보다 큰 수를 뒤에서 지워야 하는 게 아니라,
# 나중에 그 수들 가지고 더 커질 수도 있음 
# stack 아님 