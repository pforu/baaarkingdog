import sys
input = sys.stdin.readline
import bisect

T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    rst = 0
    for i in a:
        rst += bisect.bisect_left(b, i)
    ans.append(rst)
    
print(*ans, sep='\n')