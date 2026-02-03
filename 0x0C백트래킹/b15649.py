import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]*M
isused = [False]*(N+1)
ans = []

def func(k):
    if k==M:
        # print(*arr)
        ans.append(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)
print('\n'.join(ans))