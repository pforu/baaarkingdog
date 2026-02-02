import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
# 함수의 정의(인자, 어디까지 계산하고 자기한테 넘겨줄지), base condition, 재귀식

# 하나씩 곱하는 게 아님, 반씩 자르기 
# 꼭 n-1을 호출할 필요는 없음, 하나씩 내려가야 되는 게 아님 
def func(a, b, c): # a를 b번 곱한 수를 c로 나눔 
    if b==1: return a % c
    val = func(a, b//2, c) # 절반 계산 
    val = val * val % c # 제곱 
    if b%2==0: return val # 짝수지수라면 그대로 
    return val * a % c # 홀수지수라면 원래 수 한 번 더 곱하기 

print(func(A, B, C))