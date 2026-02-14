import sys
input = sys.stdin.readline
import heapq
# "수치심을 줄이고 싶을 수록 같거나 더 많은 돈이 필요하고,
# 수치심을 더 받는 것을 감수하면 같거나 더 적은 돈이 필요하게 된다는 것"
# """최대 요금의 최솟값"""
# 문제의 언급에서 이분탐색임을 알 수 있음 
INF = int(1e15) # 10만개 * 10^9원

N, M, A, B, C = map(int, input().split())
adj = [[] for _ in range(N+1)]
l, r = 0, 0
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))
    r = max(r, w)

def solve(max_money):
    d = [INF]*(N+1)
    h = []
    d[A] = 0
    heapq.heappush(h, (d[A], A))
    while h:
        cd, cn = heapq.heappop(h)
        if d[cn]!=cd: continue
        for nd, nn in adj[cn]:
            if nd > max_money: continue
            if d[nn] > cd + nd:
                d[nn] = cd + nd
                heapq.heappush(h, (d[nn], nn))
    if d[B]<=C:
        return True
    return False

rst = -1
while l<=r:
    mid = (l+r)//2
    if solve(mid):
        rst = mid
        r = mid - 1
    else:
        l = mid + 1
# 최댓값의 최솟값: 성공했을 경우 더 낮춰야 함, r = mid - 1
# 최솟값의 최댓값: 성공했을 경우 더 올려야 함, l = mid + 1
print(rst)