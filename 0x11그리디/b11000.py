import sys
input = sys.stdin.readline
import heapq

N = int(input())
lec = [list(map(int, input().split())) for _ in range(N)]
# 스케쥴링이랑 다르게, 모든 걸 다 써야 함 
lec.sort()
# 정렬+그리디-힙 :
# 제일 빨리 끝나는 걸 갈아치워도,
# 어차피 그 사이에 들어갈 건 이미 처리된 후라 그것보다 최선의 선택은 없음 

end = [] # 강의 종료시간들 
heapq.heappush(end, lec[0][1])
for s, t in lec[1:]:
    if end[0]<=s: # 가장 빨리 끝나는 강의 뒤에 가능
        heapq.heappop(end) # 갱신 
    heapq.heappush(end, t)
print(len(end))



# n^2logn이라서 n=20만에서 TLE
# room = [lec[0][1]]
# for s, t in lec[1:]:
#     room.sort()
#     pos = bisect.bisect_right(room, s)
#     if pos==0:
#         room.append(t)
#     else:
#         room[pos-1] = t
# print(len(room))