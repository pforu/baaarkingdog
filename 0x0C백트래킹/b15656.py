import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 사전 순으로 증가하는 순으로 ~ : sort 
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(N):
        rst[cnt] = arr[i]
        func(cnt+1)

func(0)
print('\n'.join(ans))