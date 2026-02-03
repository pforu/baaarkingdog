import sys
input = sys.stdin.readline

# 부분수열 : 연속X, 순서O
# 부분 문자열/배열 : 연속O, 순서O
# 부분집합 : 연속X, 순서X

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# N-Queen에서 매 행을 순서대로 보기 때문에 isused_row는 필요없음
# 이와 마찬가지로 여기서도 순서대로 리스트를 한 번씩만 보기 때문에 필요없음 
cnt = 0

def func(until, k, sum):
    if sum==M:
        global cnt
        cnt += 1
    
    for i in range(until, N):
        func(i + 1, k + 1, arr[i] + sum)
    # return

func(0, 0, 0)
print(cnt if M!=0 else cnt-1)