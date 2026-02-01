import sys
input = sys.stdin.readline
from collections import deque

# 상태를 이용 / 레이어가 있는 BFS - dist[x좌표][y좌표][z좌표][상태1][상태2]..
# 나중에 상태가 많아지면 비트마스킹 활용 
# BFS의 거리순 큐 성질을 이용해야 하기 때문에, 큐는 하나로 돌아감
# 방문 체크를 결정하는 변수가 뭔지 찾기
# 어디를 방문할 건지는 DIRS를 응용
# >> 큐는 시간의 흐름, dist는 변수에 따른 경우의 수를 담당

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)] #1이 벽

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def solve():
    # 바뀌는 것들을 함수로 묶기
    # TC마다 새로 계산되는 것들(자동 초기화), 빈번하게 참조되는 것들(지역변수 참조가 더 빠른 py 특성)
    dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    # == [[[-1 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    # >> 각 좌표에 [-1, -1] 있음, 부수지 않았을 때 / 부쉈을 때의 최단거리가 각각 저장
    Q = deque()

    dist[0][0][0] = dist[0][0][1] = 1
    # (1, 1)과 (N, M)은 항상 0이므로, dist[0][0][0] = 1만 해도 충분 
    Q.append((0, 0, 0))

    while Q:
        cx, cy, is_broken = Q.popleft()
        if cx==N-1 and cy==M-1:
            return dist[cx][cy][is_broken]
            

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy

            if 0<=nx<N and 0<=ny<M: # 파이썬은 함수 호출 비용이 큼 
                # 벽이 아닐 때 + 부순/안 부순 좌표를 처음 방문
                if board[nx][ny]==0 and dist[nx][ny][is_broken]==-1:
                    dist[nx][ny][is_broken] = dist[cx][cy][is_broken] + 1
                    Q.append((nx, ny, is_broken))
                # 벽일 때 + 벽인 좌표를 처음 방문 + 아직 부순 적 없음 
                if board[nx][ny]==1 and dist[nx][ny][1]==-1 and is_broken==0:
                    dist[nx][ny][1] = dist[cx][cy][is_broken] + 1
                    Q.append((nx, ny, 1))

    return -1

print(solve())