import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rst = [0]*M
ans = []

def func(st, cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(st, N+1):
        rst[cnt] = i
        func(i, cnt+1)

func(1, 0)
print('\n'.join(ans))