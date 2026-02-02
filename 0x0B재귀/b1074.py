import sys
input = sys.stdin.readline

# 전체(n) 속에서 부분(n-1)이 어떤 형태로 변형(사용)되는지 볼 필요가 있음 
# 최소단위를 결국 쓰겠지만, 그걸 고민하면 안 됨!
# 한 단계를 재귀함수 보이는 부분이 처리하는 것

N, R, C= map(int, input().split())

def func(n, r, c):
    if n==0: # 종료조건은 최소 단위일 때 수행할 게 뭔지 
        # n=1일 때를 생각해도 됨
        return 0
    half = 2**(n-1)
    if r<half and c<half: return func(n-1, r, c)
    elif r<half and c>=half: return half**2 + func(n-1, r, c-half)
    elif r>=half and c<half: return half**2*2 + func(n-1, r-half, c)
    return half**2*3 + func(n-1, r-half, c-half)
# z모양이 실현되는 건 half**2 * ? 을 더해주는 부분
# **은 정말 n의 m제곱인지, m의 n제곱은 아닌지 유의

print(func(N, R, C))