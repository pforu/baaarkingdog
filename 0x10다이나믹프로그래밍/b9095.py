import sys
input = sys.stdin.readline

T = int(input())
arr = [int(input()) for _ in range(T)]
d = [0, 1, 2, 4] + [0]*10 # 초기값을 어디까지 구해야 되는지 
for i in range(4, 11): # 테이블의 값을 미리 구해서 넣어놓기 
    d[i] = d[i-1] + d[i-2] + d[i-3]
ans = []
for i in arr:
    ans.append(d[i])
print('\n'.join(map(str, ans)))