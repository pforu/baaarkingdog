import sys
input = sys.stdin.readline

# 실제 큐는 안 씀, 가리키는 게 항상 하나니까 

# 사이클인데 분리문제
# 탐색의 순서를 어떻게 정하지?
# 따라가야 됨 : 그냥 가리키는 걸 큐에 넣자
# 그리고 저장해두는거임 같은 수로, 그리고 똑같은 수 다시 만나면 한 팀
# vis!=-1 하면 안됨, 다시 만나야 되니까

T = int(input())
for _ in range(T):
    N = int(input())
    point = [0]
    for val in map(int, input().split()):
    # map은 iterator이자 iterable
        point.append(val)
    vis = [0]*(N+1) # 시작점의 값을 넣는 거, 있으면 넘기기, 같으면 한바퀴 돌기

    for i in range(1, N+1):
        start = i
        while vis[i]==0:
            vis[i] = start
            i = point[i]
        if vis[i]==start: # i==start라고 쓰면 1232를 못 잡음 
            while vis[i]!=-1:
                vis[i] = -1 #freeze
                i = point[i]
    # print(vis)

    cnt = 0
    for i in range(1, N+1):
        if vis[i]!=-1:
            cnt += 1
    print(cnt)
    # 야 백트래킹 있어야 되는데? 어캄?
    # 가능한 애들부터 보고 되면 freeze를 해줘야 되는데 한꺼번에 

    # > BFS를 여러 시작점에 대해서 진행해야 할 때
    # > visited 배열을 매번 새로 만들거나 초기화를 시키면 O(N^2)이 되지만
    # > visited 여부를 체크하는 값을 매번 다른 값을 넣어 O(N)으로 만드는 테크닉
    # > 그래프라는 자료구조에서 중복 방문을 막으면서
    # > 사이클(특정 상태)을 어떻게 찾아낼 것인가라는 탐색의 본질

    # 백트래킹이 아니라 걍 선형으로 진행하되, 맵을 두 개 쓰면 되지
    # 값이 들어가 있기만 하면 간 곳이고, 사이클인지는 따로 저장하면 되니까
    # > 그 값을 특정 값(-1)으로 저장(freeze)하면 사이클 맵이 따로 필요 없음 
    # 그럼 본인을 발견했을 때 사이클은 어떻게 저장할 건데
    
    # > 그 지점부터 한바퀴 더 돌면서 vis에 저장하는 거
    # > 굳이 재귀 안 쓰니까 백트래킹보다 나음
