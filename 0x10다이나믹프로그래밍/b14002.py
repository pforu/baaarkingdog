import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

route = [0]*(N+1) 
d = [0]*(N+1)

for i in range(1, N+1):
    d[i] = 1
    route[i] = -1
    for j in range(1, i):
        if arr[j]<arr[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            route[i] = j

length = max(d)
pos = d.index(length)
rst = []
for _ in range(length): # 따라가기 
    rst.append(arr[pos])
    pos = route[pos]
print(length)
print(*rst[::-1])