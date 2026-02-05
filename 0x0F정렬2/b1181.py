import sys
input = sys.stdin.readline

N = int(input())
words = list(set([input().strip() for _ in range(N)]))
words.sort(key=lambda x: (len(x), x))
print(*words, sep='\n')