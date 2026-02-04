import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
isused = [False for _ in range(N)]
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(N):
        if not isused[i]:
            isused[i] = True
            rst[cnt] = arr[i]
            func(cnt+1)
            isused[i] = False

func(0)
print('\n'.join(ans))