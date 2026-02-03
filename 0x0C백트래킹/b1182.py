import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def func(k, sum):
    global cnt
    if k==N: # 아무튼 끝까지 가면 
        if sum==M:
            cnt += 1
        return
    
    # 이진상태트리
    func(k+1, sum) # 이번 거 안 더함 
    func(k+1, arr[k]+sum)

    # 이전 연습문제들은 이번 칸에 둘 여러 후보 중 하나를 골라야 됨 
    # 이건 이번 칸에 얘를 포함할지 말지만 결정하면 돼서 2개를 돌림
    # 그걸 형태상 for문이 아니고 func() 2번 호출로 구현한 것 

func(0, 0)
print(cnt if M!=0 else cnt-1)