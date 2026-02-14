import sys
input = sys.stdin.readline

K, L = map(int, input().split())
d = dict()
for i in range(L):
    d[input().strip()] = i
sort_dict = sorted(d.items(), key=lambda x: x[1])[:K]
print('\n'.join([x[0] for x in sort_dict])) # 리스트 컴프리헨션 잘 쓰기 