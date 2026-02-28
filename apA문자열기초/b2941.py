import sys
input = sys.stdin.readline

lst1 = ['dz=', 'lj', 'nj']
lst2 = ['c=', 'c-', 'd-', 's=', 'z=']
inp = input().strip()

f = [False]*(len(inp))
rst = 0
for lst in [lst1, lst2]:
    for l in lst:
        idx = 0
        while True:
            idx = inp.find(l, idx)
            if idx==-1: break
            if not any(f[idx: idx+len(l)]): 
                for i in range(idx, idx+len(l)):
                    f[i] = True
                rst += 1
            idx += len(l)
rst += f.count(False)
print(rst)