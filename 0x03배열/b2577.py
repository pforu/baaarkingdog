import sys
input = sys.stdin.readline

# 1,000 ^3
count = [0]*10
num = 1
for _ in range(3):
    num*=int(input())
for i in list(str(num)):
    count[int(i)] += 1

print(*count, sep='\n')