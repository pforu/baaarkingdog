import sys
input = sys.stdin.readline

# 1. 모든 조합 생성 - 재귀?
# 2. dp - d[i] = 값이 i일 때의 최솟값 (사실상 1번 탐색에 n번 소요)
# 3. 그리디 - 배수니까, 제일 큰 것부터 쓰면 됨

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

cnt = 0
for i in range(N-1, -1, -1):
    cnt += K//arr[i]
    K %= arr[i]
print(cnt)