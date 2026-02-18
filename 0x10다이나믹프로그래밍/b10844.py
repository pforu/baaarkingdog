import sys
input = sys.stdin.readline
# arr/tmp : i로 끝나는 계단수의 개수 

N = int(input())
arr = [0]*2 + [1]*9 + [0] # 앞뒤에 0 붙여서 0과 9 예외처리 없앰 
for i in range(N-1):
    tmp = [0]*12
    for j in range(1, 11):
        tmp[j] = arr[j-1] + arr[j+1]
        # 이번에 끝이 n으로 끝나는 걸 만들 수 있는 건
        # 저번에 끝이 n-1, n+1로 끝났던 것들 
        # 0은 1만이 만들 수 있고, 9는 8만이 만들 수 있음
    arr = tmp[:]
print(sum(arr) % 1000000000)

# 한 단계의 변화만 그려보기, 전체 말고 필요한 부분만 떼서.
# 바뀌는 부분을 먼저 파악하기 