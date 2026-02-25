import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(2)]

    d = [[0]*(N+1) for _ in range(3)]
    d[0][1], d[1][1], d[2][1] = 0, board[1][1], board[2][1]
    for i in range(2, N+1):
        d[0][i] = max(d[0][i-1], d[1][i-1], d[2][i-1])
        d[1][i] = max(d[2][i-2], d[1][i-2], d[0][i-1], d[2][i-1]) + board[1][i]
        d[2][i] = max(d[2][i-2], d[1][i-2], d[0][i-1], d[1][i-1]) + board[2][i]
    ans.append(max(d[0][N], d[1][N], d[2][N]))
print('\n'.join(map(str, ans)))
# n=1일 때 등 범위의 최대최소값은 항상 확인 



# 어차피 최댓값을 구하는 문제이기 때문에,
# i열에서 아무것도 안 뗄 거라면 i-1열에서 이미 위든 아래든 떼어놓은 상태가 무조건 더 이득
# 따라서 0배열은 필요없음 

# for i in range(2, N+1):
#     # 위쪽을 뗄 때: (대각선 아래 직전) vs (그 전 열에서 가장 컸던 값)
#     d[1][i] = max(d[2][i-1], d[1][i-2], d[2][i-2]) + board[1][i]
#     # 아래쪽을 뗄 때: (대각선 위 직전) vs (그 전 열에서 가장 컸던 값)
#     d[2][i] = max(d[1][i-1], d[1][i-2], d[2][i-2]) + board[2][i]


### 바킹독 정해 
# dp[i][j] : i번째 열까지에서 점수의 최댓값, 단 j행 i열의 스티커는 반드시 선택

# 가장 직전에 붙인 스티커가 i-2열의 스티커인 경우 : max(dp[i - 2][0], dp[i - 2][1]) + arr[i][j]
# 가장 직전에 붙인 스티커가 i-1열의 스티커인 경우 : dp[i-1][1-j] + arr[i][j]

# 마지막 열에 있는 스티커 중 어느 하나는 반드시 붙인게 최댓값이므로 max(dp[N - 1][0], dp[N - 1][1])을 계산