import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    combined = sorted([(x, 0) for x in A] + [(x, 1) for x in B])

    cnt = 0
    rst = 0
    for i in combined:
        if i[1]==1:
            cnt += 1
        if i[1]==0:
            rst += cnt
    ans.append(rst)

print(*ans, sep='\n')