import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # 사전 순으로 증가하는 순으로 ~ : sort 
rst = [0]*M
ans = []

def func(st, cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(st, N): # 고른 수열은 비내림차순 : st부터 탐색 
        rst[cnt] = arr[i]
        func(i, cnt+1) # 같은 수를 여러 번 골라도 된다 : not i+1

func(0, 0)
print('\n'.join(ans))