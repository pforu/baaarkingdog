import sys
input = sys.stdin.readline

N = int(input())
isused_col = [False for _ in range(N)]
isused_up = [False for _ in range(2*N)]
isused_down = [False for _ in range(2*N)]

cnt = 0

def func(k):
    if k==N:
        global cnt # 함수 사용 시 항상 신경쓰기 
        cnt += 1 # 불변 객체 재할당
        return
    
    for i in range(N):
        if isused_col[i] or isused_up[k + i] or isused_down[k - i + N - 1]:
            continue
        isused_col[i] = True
        isused_up[k + i] = True
        isused_down[k - i + N - 1] = True
        func(k+1)
        isused_col[i] = False
        isused_up[k + i] = False
        isused_down[k - i + N - 1] = False

func(0)
print(cnt)