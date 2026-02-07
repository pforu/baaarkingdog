import timeit
from itertools import product

# 1. 진법 연산 방식 (Manual Base Conversion)
def manual_loop():
    n = 10  # CCTV 10개 가정
    for i in range(1 << (2 * n)):
        tmp = i
        dirs = []
        for _ in range(n):
            dirs.append(tmp % 4)
            tmp //= 4

# 2. itertools.product 방식
def itertools_loop():
    n = 10
    for dirs in product(range(4), repeat=n):
        pass

# 각 함수를 10번씩 돌려서 평균 시간 측정
t1 = timeit.timeit(manual_loop, number=1)
t2 = timeit.timeit(itertools_loop, number=1)

print(f"진법 연산: {t1:.5f}초")
print(f"itertools: {t2:.5f}초")