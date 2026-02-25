import sys
input = sys.stdin.readline

N = int(input())
n = abs(N)

d = [0, 1, 1] + [0]*n
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]) % 1000000000

print(-1 if N<0 and N%2==0 else (0 if N==0 else 1))
print(d[n])

### 출력 형식 제발 잘 읽기 
# 첫째 줄에 F(n)이 양수이면 1, 0이면 0, 음수이면 -1을 출력한다. : n이 아니라, F(n)
# 둘째 줄에는 F(n)의 절댓값을 출력한다. : 값이 아니라, 절댓값 
# 이 수가 충분히 커질 수 있으므로, 절댓값을 1,000,000,000으로 나눈 나머지를 출력한다.