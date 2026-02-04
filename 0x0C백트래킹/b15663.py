import sys
input = sys.stdin.readline

# 같은 값이 섞여 있다면?
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split()))) # sort를 써야 중복수가 있다면 직전값임이 보장 
isused = [False for _ in range(N)]
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst)))
        return
    
    before = -1 # 다음 레벨에서는 새로 생성, 레벨끼리 독립적 
    for i in range(N): 
        if not isused[i] and before!=arr[i]:
            isused[i] = True
            before = arr[i] # 한 레벨마다 방금 이 자리에 누가 있었는지를 저장
            rst[cnt] = arr[i]
            func(cnt+1)
            isused[i] = False

func(0)
print('\n'.join(ans))