import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
# 중복조합은 똑같은 수를 제한 없이 여러 번 선택 가능하기 때문에 set을 여기서 쓰는 게 효율적 
ans = []

# 중복된 수는 중복된 만큼 사용할 수 있지만, 그들이 쓰인 순서에 따른 결과적 차이를 두지 않음 
for p in sorted(product(arr, repeat=M)): # 여기서 set(product) 쓰면 시간 두 배 걸림 
    ans.append(' '.join(map(str, p)))
    
print('\n'.join(ans))
