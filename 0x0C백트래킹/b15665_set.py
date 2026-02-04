import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split())))) # 같은 수를 여러 번 골라도 된다 : set
N = len(arr)
rst = [0]*M
ans = []

def func(cnt):
    if cnt==M:
        ans.append(' '.join(map(str, rst))) # 2. 여기서 인덱스 참고해서 값을 뽑는 것도 가능
        # 3. 다만 파이썬은 print가 느려서 join을 써야 되니까 어차피 배열에 넣게 됨, 무쓸모 
        return
    
    for i in range(N):
        rst[cnt] = arr[i] # 1. 여기서 i를 넣고 
        func(cnt+1)

func(0)
print('\n'.join(ans))