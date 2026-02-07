import sys
input = sys.stdin.readline
# 시간끌지 말고 적당히 구하면 검증하기

T = int(input())
d = [0, 1, 1, 1, 2, 2] + [0]*100
for i in range(6, 101):
    d[i] = d[i-1] + d[i-5]

ans = []
for _ in range(T):
    ans.append(d[int(input())])
print('\n'.join(map(str, ans)))