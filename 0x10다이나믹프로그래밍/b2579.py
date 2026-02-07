import sys
input = sys.stdin.readline

# 테이블 정의 시, 필요한 정보를 n차원 배열을 써서 담아두기 (like BFS)
N = int(input())
arr = [0] + [int(input()) for _ in range(N)] + [0]*3 # N=1일 때 d 초기화에서 arr[2] 접근 불가 
d = [[0, 0, 0], [0, arr[1], 0], [0, arr[2], arr[1]+arr[2]]] + [[0]*3 for _ in range(N)]

for i in range(3, N+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + arr[i]
    d[i][2] = d[i-1][1] + arr[i]

print(max(d[N]))