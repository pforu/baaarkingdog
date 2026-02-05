import sys
input = sys.stdin.readline
from collections import Counter

N, C = map(int, input().split())
arr = Counter(map(int, input().split()))

sorted_items = sorted(arr.items(), key=lambda x:x[1], reverse=True)

ans = []
for num, freq in sorted_items:
    ans.extend([num]*freq)

print(*ans)

# from collections import Counter

# lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# # 1. 생성: 리스트를 던지면 바로 빈도수 딕셔너리가 됨
# c = Counter(lst)
# print(c)  # Counter({4: 4, 3: 3, 2: 2, 1: 1})

# # 2. most_common(n): 가장 많이 나온 요소 n개를 빈도순으로 반환
# print(c.most_common(2))  # [(4, 4), (3, 3)]

# # 3. elements(): 개수만큼 반복되는 반복자(iterator) 반환
# # 다시 원래 리스트 형태로 복구할 때 유용
# print(list(c.elements()))  # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


# ################################################

# # 정렬 기준: 오직 빈도수(내림차순)만 명시
# # counts는 등장 순서를 기억하므로, 빈도가 같으면 먼저 들어온 순서가 유지됩니다.
# # (파이썬의 sort는 Stable Sort이기 때문)
# unique_nums = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

# for num in unique_nums:
#     print(f"{num} " * counts[num], end="")
