import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    
    before = -1
    for i in range(N): # 처음부터 도는 것 : 다음 레벨에서 이 숫자를 이번 인덱스 거든 다음 인덱스 거든
        # 다시 쓰는 건 상관없음, isused 체크 없이.
        if arr[i]!=before:
            before = arr[i] # 이번 레벨에서 이 숫자는 다시 여기에 안 앉힘 
            rst[cnt] = arr[i]
            func(cnt+1)

func(0)
print('\n'.join(ans))