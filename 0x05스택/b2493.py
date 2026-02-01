import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
tow = list(map(int, input().split()))

stack = deque()
# 높이는 다 다름 
# 오큰수랑 똑같은 거 아닌가 근데 왼큰수인 거지 
# 나보다만 크면 되네 근데
# 특징: 답은 들어올 때 바로 결정됨, 스택 유지만 신경쓰기 

rst = [0]*N
for i, val in enumerate(tow):
    while stack and tow[stack[-1]]<val:
        stack.pop()
    if stack:
        rst[i] = stack[-1]+1
    stack.append(i)

print(*rst)

# 6이 들어오면 앞에 아무것도 없고 
# 9가 들어오면 6이 안 크고 : 6을 빼 
# 5가 들어오면 9에 부딪힘 > 이걸 어떻게 하지? : 남은 게 9잖아 
# 7이 들어오면 9에 부딪힘 > 이거 : 5를 빼고(왜냐면 7 뒤는 다 7이니까) 남은 거 9
# 4는 9, 7 스택에서 7