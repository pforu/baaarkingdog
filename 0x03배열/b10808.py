import sys
input = sys.stdin.readline

alpha = [0]*26
inp = list(input().strip())

for a in inp:
    alpha[ord(a)-ord('a')] += 1

print(*alpha)