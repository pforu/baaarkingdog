import sys
input = sys.stdin.readline

N = int(input())
pat = input().strip()
lenpat = len(pat)-1
sppat = pat.split('*')
for _ in range(N):
    inp = input().strip()
    print('DA' if inp.startswith(sppat[0]) and inp.endswith(sppat[-1]) and len(inp)>=lenpat else 'NE')


# import re
# # 별표가 여러 개인 경우의 예시
# regex = re.compile('^' + pat.replace('*', '.*') + '$')
# if regex.match(inp):
#     print('DA')