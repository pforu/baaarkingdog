import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + [int(input()) for _ in range(N)] + [0]*5 # 1-indexed로 할 거니까 처리 잘 해주기
d = [0, arr[1], arr[2], arr[3]] + [0]*N # 점화식에 쓰이는 만큼 초기값 설정 

for i in range(4, N+1): # 1-indexed로 할 거니까 처리 잘 해주기
    d[i] = min(d[i-2], d[i-3]) + arr[i]

print(sum(arr) - min(d[N-1], d[N-2]))