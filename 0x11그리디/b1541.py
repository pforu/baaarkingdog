import sys
input = sys.stdin.readline

# 그리디인 이유: +-만 있으니까

sen = list(input().strip())
sen.reverse()
num = []
col = 0
rst = 0
for s in sen:
    if s=='-':
        col += int(''.join(map(str, num[::-1])))
        num = []
        rst -= col
        col = 0
    elif s=='+':
        col += int(''.join(map(str, num[::-1])))
        num = []
    else:
        num.append(s)
rst += int(''.join(map(str, num[::-1])))
rst += col
print(rst)