import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    rec = input().split()
    others = []
    rst = []

    while True:
        inp = input().split()
        if inp[0]=='what':
            break
        others.append(inp[-1])

    for sound in rec:
        if sound not in others:
            rst.append(sound)
    
    print(' '.join(rst))