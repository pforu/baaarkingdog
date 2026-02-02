import sys
input = sys.stdin.readline

N = int(input())
# 함수의 정의(인자, 어디까지 계산하고 자기한테 넘겨줄지), base condition, 재귀식
# 재귀는 전체 속에서 부분을 쓸 때, 그 로직을 믿는 것

rst = []

def solve(n, a, b): # n개 원판을 a에서 b로 옮기는 과정 서술 
    if n==1:
        rst.append((a, b)) # 1개 원판은 a에서 b로 바로 옮기면 됨 
        return
    solve(n-1, a, 6-a-b) # n-1개 원판을 a에서 ?로 치워두는 과정 서술 
    rst.append((a, b)) # 치워뒀으니까, n번째 원판을 a에서 b로 옮기기 
    solve(n-1, 6-a-b, b) # n-1개 원판을 ?에서 b로 치워두는 과정 서술 

solve(N, 1, 3)
print(len(rst))
print("\n".join(f"{i} {j}" for (i, j) in rst))