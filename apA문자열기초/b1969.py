import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = [{'A':0, 'C':0, 'G':0, 'T':0} for _ in range(M)]

for _ in range(N):
    inp = input().strip()
    for i, d in enumerate(inp):
        dna[i][d] += 1
        
ans = []
rst = 0
for lst in dna:
    mindna = sorted(lst.items(), key=lambda x: (-x[1], x[0]))[0]
    ans.append(mindna[0])
    rst += (sum(lst.values()) - mindna[1])
print(''.join(ans), rst, sep='\n')