import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    bidx = 0
    rst = 0
    for aidx in range(N): # 모든 값에 대해 탐색할 애가 누군지 찾기 
        while bidx<M and a[aidx]>b[bidx]:
            bidx += 1 # bidx가 끝까지 가면 M이므로 
        rst += bidx # while도 안 돌고 값도 맞음 
    ans.append(rst)

print(*ans, sep='\n')