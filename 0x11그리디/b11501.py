import sys
input = sys.stdin.readline

# max보다 작은 건 무조건 사서 max에 파는 게 이득
# 그 이후에는 지역적으로 다시 max 구해서..

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # max()가 O(n)이므로 저장해놓기 
    til = []
    num = arr[-1]
    for val in arr[::-1]:
        if val>num:
            num = val
        til.append(num)
    til.reverse()

    money = 0
    cnt = 0
    for i, val in enumerate(arr):
        if val!=til[i]:
            money -= val
            cnt += 1
        else:
            money += til[i]*cnt
            cnt = 0

    ans.append(money)
print('\n'.join(map(str, ans)))