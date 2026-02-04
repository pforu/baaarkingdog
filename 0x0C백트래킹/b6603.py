import sys
input = sys.stdin.readline

rst = [0]*6
ans = []

def func(n, st, cnt):
    if cnt==6:
        ans.append(' '.join(map(str, rst)))
        return
    for i in range(st, n):
        rst[cnt] = arr[i]
        func(n, i+1, cnt+1)
    
while True:
    line = list(map(int, input().split()))
    k = line[0]
    if k==0:
        break
    arr = line[1:]

    func(k, 0, 0)
    ans.append('')

print('\n'.join(ans))