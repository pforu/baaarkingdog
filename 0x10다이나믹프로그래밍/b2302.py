import sys
input = sys.stdin.readline
### 접근 잘 함, 점화식의 당위성과 예외처리 신경쓰기 
N = int(input())
M = int(input())
vip = [0] + [int(input()) for _ in range(M)] + [N+1]

seq = []
for i in range(M+1):
    inter = vip[i+1] - vip[i] - 1
    if inter!=0:
        seq.append(inter)

d = [0, 1, 2] + [0]*N
for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

ans = 1
for s in seq:
    ans *= d[s]
print(ans)