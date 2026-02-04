import sys
input = sys.stdin.readline
from itertools import combinations

ans = []
    
while True:
    line = list(map(int, input().split()))
    k = line[0]
    if k==0:
        break
    arr = line[1:]

    for c in combinations(arr, 6):
        ans.append(' '.join(map(str, c)))
    ans.append('') # 맨 마지막에 빈 줄 하나 더 들어감

print('\n'.join(ans)) # print('\n'.join(ans).strip())으로 제거 가능 

# 이건 백트래킹 코드랑 메모리/시간 완전 동일 