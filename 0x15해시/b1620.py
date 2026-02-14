import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict1 = dict()
dict2 = dict()
for i in range(1, N+1):
    val = input().strip()
    dict1[str(i)] = val
    dict2[val] = str(i)

ans = []
for i in range(M):
    val = input().strip()
    rst = dict1.get(val) if val in dict1 else dict2.get(val)
    ans.append(rst)
print('\n'.join(ans))