import sys
input = sys.stdin.readline

N = int(input())
stu = list(map(int, input().split()))

### 가장 긴 연속수열 찾기
# 수가 1에서 N까지로 정해져 있기 때문에 그때까지 앞에서 나온 학생 수를
# d 테이블에 저장

d = [0]*(N+1)
for i in stu:
    d[i] = d[i-1] + 1

print(N - max(d))


# 100만이므로 nlogn, heap 써도 안됨 
# d = [0]*(N+1)
# h = []
# for i in range(1, N+1):
#     tmp = []
#     while h and h[0][1] > stu[i]:
#         tmp.append(heapq.heappop(h))
#     if h:
#         d[i] = -h[0][0] + 1
#         heapq.heappush(h, (-d[i], stu[i]))
#     else:
#         d[i] = 1
#         heapq.heappush(h, (-1, stu[i]))
#     for val in tmp:
#         heapq.heappush(h, val)
    
# # print(d)
# print(N - max(d))