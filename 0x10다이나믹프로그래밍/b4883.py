import sys
input = sys.stdin.readline

INF = int(1e9) # inf 정의 제대로 하기 
ans = []
tc = 0
while True:
    tc += 1
    N = int(input())
    if N==0:
        break

    board = [[0]*5] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    # 패딩 리스트컴프리헨션 문법 주의 
    d = [[INF]*5 for _ in range(N+1)]

    d[1][2], d[1][3] = board[1][2], board[1][2] + board[1][3] # d에서 초기값 어디까지 설정해야 하는지
    # d[1][1]은 INF 초기화이므로 자동으로 최솟값에서 걸러짐 

    for i in range(2, N+1): # 2~N
        for j in range(1, 4): # 1~3
            minbef = min(d[i-1][j-1], d[i-1][j], d[i-1][j+1], d[i][j-1]) # DIRS가 아니라 바로 하는 것 
            d[i][j] = minbef + board[i][j]
    # print(d)
    ans.append(f"{tc}. {d[N][2]}") # f 밖으로 빼는 거 
print('\n'.join(ans))