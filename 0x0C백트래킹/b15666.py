import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split())))) # 같은 수를 여러 번 골라도 된다 : set
N = len(arr) # 얘는 신경쓰기 
rst = [0]*M
ans = []

def func(st, cnt): # 비내림차순 : st 
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(st, N): 
        rst[cnt] = arr[i]
        func(i, cnt+1)

func(0, 0)
print('\n'.join(ans))