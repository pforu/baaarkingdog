import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]

# 1. 함수 정의 
# def serial_key(s):
#     total_sum = 0
#     for char in s:
#         if char.isdigit():
#             total_sum += int(char)

#     return (len(s), total_sum, s)

# arr.sort(key=serial_key)

# 2. pythonic
arr.sort(key=lambda x: (len(x), sum(int(i) for i in x if i.isdigit()), x))
print(*arr, sep='\n')

# 3. if 문자>숫자 순서일 때(아스키의 반대)
# arr.sort(key=lambda x: (
#     len(x), 
#     sum(int(i) for i in x if i.isdigit()), 
#     [(0, c) if c.isalpha() else (1, c) for c in x]
# ))