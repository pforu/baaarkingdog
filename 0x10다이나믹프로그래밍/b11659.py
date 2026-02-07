import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split())) # prefix-sum은 무조건 1-indexed 
d = [0]*(N+1) # N+1 주의 

for i in range(1, N+1): # N+1 주의 
    d[i] = d[i-1] + arr[i]

ans = []
for i in range(M):
    a, b = map(int, input().split())
    ans.append(d[b]-d[a-1]) # (end) - (start-1)
print('\n'.join(map(str, ans))) # join은 str 