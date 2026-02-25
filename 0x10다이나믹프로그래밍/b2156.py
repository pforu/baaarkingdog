import sys
input = sys.stdin.readline
# 연속 3계단 안되는 문제랑 비슷
# 단, 마지막을 꼭 선택해야 한다는 조건이 없으며 최대간격 조건도 없음 

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

if N==1:
    print(arr[1])
else:
    d = [[0, 0, 0], [0, arr[1], 0], [arr[1], arr[2], arr[1]+arr[2]]] + [[0]*3 for _ in range(N-2)]

    for i in range(3, N+1):
        d[i][2] = d[i-1][1] + arr[i]
        d[i][1] = max(max(d[i-2]), d[i-1][0]) + arr[i]
        d[i][0] = max(max(d[i-2]), max(d[i-1])) # 이걸 선택하지 않았을 경우도 고려할 것 
    # print(d)
    print(max(d[N]))

# 포도주 양은 0 이상, 잔의 개수는 1 이상
# 최소, 최대, 경계값에 대해서 생각을 꼭 하기 
