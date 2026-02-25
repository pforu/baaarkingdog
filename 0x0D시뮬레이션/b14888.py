import sys
input = sys.stdin.readline
import math
from collections import Counter
from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
op_raw = list(map(int, input().split())) # + - * /
oplst = Counter({x:o for x, o in enumerate(op_raw)}).elements()

maxans, minans = -int(1e10), int(1e10)
opset = set(permutations(oplst)) # 중복을 아예 안 만들고 싶으면 dfs로 남은 연산자 개수 확인하면서 
for c in opset:
    rst = num[0]
    idx = 1
    for op in c:
        val = num[idx]
        match op:
            case 0:
                rst += val
            case 1:
                rst -= val
            case 2:
                rst *= val
            case 3: # int(rst/val) : int()는 0 쪽으로 소수점을 버림, 양수와 음수 모두 충족 
                if rst > 0:
                    rst //= val
                else:
                    rst = math.ceil(rst/val)
        idx += 1
    maxans, minans = max(maxans, rst), min(minans, rst)
print(maxans, minans, sep='\n')