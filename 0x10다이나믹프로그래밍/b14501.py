import sys
input = sys.stdin.readline
# d : 역방향, 오늘 상담을 하는 경우와 안 하는 경우 중 max를 담음

N = int(input())
t = [0]*(N+1)
p = [0]*(N+1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

d = [0]*(N+3)
for i in range(N, 0, -1):
    d[i] = d[i+1] # 아래 if문의 else로 빼도 됨 
    if i+t[i]-1<=N:
        d[i] = max(p[i] + d[i+t[i]], d[i+1])
        # 오늘 상담을 함 : 상담 끝난 다음 날짜 이익 + 이번상담이익 
        # 오늘 상담을 안 함 : 내일이익 
print(d[1])