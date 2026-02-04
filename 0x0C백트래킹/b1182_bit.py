import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

# 1. 모든 부분집합의 개수(2^N)만큼 루프를 돕니다.
# 1 << N은 2의 N승과 같습니다. (N=20이면 1,048,576번)
for i in range(1, 1 << N): # 0은 공집합이므로 1부터 시작
    current_sum = 0
    
    # 2. i라는 정수의 각 비트를 검사합니다.
    for j in range(N):
        # i의 j번째 비트가 1인지 확인 (AND 연산)
        if i & (1 << j):
            current_sum += arr[j]
            
    # 3. 합이 S와 같다면 카운트
    if current_sum == S:
        count += 1

print(count)