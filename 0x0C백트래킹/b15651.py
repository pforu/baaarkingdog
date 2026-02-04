import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(1, N+1):
        rst[cnt] = i
        func(cnt+1)

func(0)
print('\n'.join(ans))