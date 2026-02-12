import sys
input = sys.stdin.readline
import heapq
# 큐 2개 사용하는 에디터 문제와 원리 동일
# 중간에서 왔다갔다 해야 되면 그거 기준으로 양옆 분리해서 생각해보기

# 일단 개수 맞춰 넣기, 잘못됐을 경우 교환 
N = int(input())
heap1, heap2 = [], []
ans = []

for i in range(N):
    inp = int(input())
    if len(heap1)==len(heap2):
        heapq.heappush(heap1, -inp)
    else:
        heapq.heappush(heap2, inp)

    if heap2 and -heap1[0]>heap2[0]:
        a = -heapq.heappop(heap1)
        b = heapq.heappop(heap2)
        heapq.heappush(heap1, -b)
        heapq.heappush(heap2, a)

    # print(heap1, heap2)
    ans.append(-heap1[0])

print('\n'.join(map(str, ans)))