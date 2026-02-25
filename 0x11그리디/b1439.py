import sys
input = sys.stdin.readline

S = input().strip()
cnt = 0
for i in range(1, len(S)):
    if S[i-1]!=S[i]:
        cnt += 1
print((cnt+1)//2) # 식 제대로 생각하기 
# 경계 개수가 cnt, 덩어리 개수가 cnt+1
# 한 번 뒤집으면 양 끝을 제외하고 경계가 2개씩 사라짐 
# 사실 0 덩어리와 1 덩어리의 개수 중 더 작은 걸 고름 