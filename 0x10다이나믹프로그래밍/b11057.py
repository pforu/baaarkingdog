import sys
input = sys.stdin.readline

N = int(input())
d = [[0]*10] + [[1]*10] + [[0]*10 for _ in range(N)]
for i in range(2, N+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][:j+1]) % 10007
print(sum(d[N])%10007) # 마지막에 한번 더 나머지연산. 여러 TC로 확인하기 
