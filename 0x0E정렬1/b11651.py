import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x: (x[1], x[0]))
### 우선순위대로 튜플 만들기, 길이는 짧은 것/ 값은 작은 것이 오름차순(기본)
### 내림차순이 필요한 수에는 마이너스

print('\n'.join(map(lambda x: f"{x[0]} {x[1]}", arr)))
# 출력 방식 기억해 두기 