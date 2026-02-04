import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
rst = [0]*M
ans = []

def func(st, cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    
    before = -1
    for i in range(st, N):
        if arr[i]!=before:
            before = arr[i]
            rst[cnt] = arr[i]
            func(i+1, cnt+1)

func(0, 0)
print('\n'.join(ans))