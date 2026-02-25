import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
# 최대한 작은 수 2개를 택하는 게 좋음 (다 합해지기 때문)

heapq.heapify(cards)
for _ in range(M):
    s = heapq.heappop(cards) + heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, s)
print(sum(cards))

# x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
# 문제 잘 읽기. 같은 카드면 안 된다는 건데 쓰인 수가 달라야 된다고 읽음 