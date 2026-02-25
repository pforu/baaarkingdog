import sys
input = sys.stdin.readline
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 가지치기 - 보드 최댓값
max_element = max(map(max, board))
# max_element = max([max(row) for row in board])

def dfs(cx, cy, tet, num, sum):
    global ans
    
    # 가지치기 - 남은 칸을 최댓값으로 채워도 갱신 못 할 거면 그냥 종료
    if sum + max_element * (4 - num) <= ans:
        return
    
    if num==4:
        ans = max(ans, sum)
        return
    for dx, dy in DIRS:
        nx, ny = cx + dx, cy + dy
        if 0<=nx<N and 0<=ny<M and not tet[nx][ny]:
            tet[nx][ny] = True # 어쨌든 nx, ny로 가는 건 맞음 
            if num==2:
                dfs(cx, cy, tet, num+1, sum+board[nx][ny])
            dfs(nx, ny, tet, num+1, sum+board[nx][ny])
            tet[nx][ny] = False   
              
            # 원래 코드   
            # if num==2: # 모양 보고 이렇게 
            #     tet[nx][ny] = True
            #     dfs(cx, cy, tet, num+1, sum+board[nx][ny])
            #     tet[nx][ny] = False          
            # tet[nx][ny] = True
            # dfs(nx, ny, tet, num+1, sum+board[nx][ny])
            # tet[nx][ny] = False       

ans = 0
tet = [[False]*M for _ in range(N)] # 이차원배열은 생성/참조/수정횟수 최대한 줄이기 
for i in range(N):
    for j in range(M):
        tet[i][j] = True
        dfs(i, j, tet, 1, board[i][j])
        tet[i][j] = False

print(ans)