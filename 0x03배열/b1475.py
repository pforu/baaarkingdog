import sys
input = sys.stdin.readline
import math

#시간제한, 메모리제한부터 보는 것 / 문제 읽고 최대 N 계산하는 것 습관들이기
# 문제가 간단해도!
# N=100만 - NlgN

N = input().strip()
count = [0]*10
for n in list(N):
    count[int(n)] += 1
count[6] = math.ceil((count[6]+count[9])/2)
count[9] = 0
#파이썬의 round()는 .5의 반올림을 짝수 쪽으로 함

print(max(count))