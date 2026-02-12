import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = [] # 빈 힙 선언은 리스트로
ans = []

for _ in range(N):
    inp = int(input())
    if inp==0:
        ans.append(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(inp), inp))
    # 힙 관련 함수는 heapq부터 쓰고 시작 

print("\n".join(map(str, ans)))