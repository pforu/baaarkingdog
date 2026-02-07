import sys
input = sys.stdin.readline

n = int(input())
d = [0, 0] + [0]*n
route = [0]*(n+3)

for i in range(2, n+1):
    # float('inf')는 비용이 큼 
    rst = d[i-1]
    route[i] = i-1
    if i%3==0:
        if d[i//3]<rst:
            rst = d[i//3]
            route[i] = i//3
    if i%2==0:
        if d[i//2]<rst:
            rst = d[i//2]
            route[i] = i//2
    d[i] = rst + 1

print(d[n])
ans = []
while n!=0:
    ans.append(n)
    n = route[n]
print(*ans)