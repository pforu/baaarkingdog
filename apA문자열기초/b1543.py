import sys
input = sys.stdin.readline

string = input().strip()
pat = input().strip()
# f = 0
# rst = 0
# while True:
#     f = string.find(pat, f)
#     if f==-1:
#         break
#     rst += 1
#     f += len(pat)
rst = string.count(pat)
print(rst)