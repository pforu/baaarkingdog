### 퇴사1과 동일한 코드로 풀었음
### 이건 앞에서 채워나가는 DP

import sys
input = sys.stdin.readline
# d : 오늘의 상담을 끝내기 전까지의 오늘의 최대 이익 

N = int(input())
t = [0]*(N+1)
p = [0]*(N+1)
for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

d = [0]*(N+3)
for i in range(1, N+1):
    d[i] = max(d[i], d[i-1]) # 어제까지의 상담을 끝낸 오늘의 수익 확정, 오늘 끝나는 상담 반영x
    if i+t[i]-1<=N:
        d[i+t[i]] = max(d[i+t[i]], p[i] + d[i])
        # 오늘 상담을 함 : 상담 끝난 '다음' 날에 미리 채워둠 
        # 오늘 상담을 안 함 : 어제의 이익과 같음 
print(max(d[N], d[N+1])) # 마지막의 다음 날에 정산이 끝나는 경우 발생 가능 