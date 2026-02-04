import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)] # 굳이 배열 만들 필요 없이, 14줄에서 arr[i] 대신 i 쓰면 됨 
rst = [0]*M
ans = []

def func(st, cnt):# k: 어디서부터 볼지(직전 값 초과), cnt: 지금까지 몇 개 뽑았는지 
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(st, N):
        rst[cnt] = arr[i]
        func(i+1, cnt+1)

func(0, 0)
print('\n'.join(ans))