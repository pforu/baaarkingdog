import sys
input = sys.stdin.readline

N = int(input())
end = [0]*N
wei = [0]*N
for i in range(N):
    end[i], wei[i] = map(int, input().split())
rst = 0

def func(idx, broken):
    global rst
    if idx==N: # 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우
        rst = max(rst, broken)
        return # 계란을 치는 과정을 종료한다
    if end[idx]<=0 or broken==N-1: # 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면
        ### 재귀문제는 모든 명시적 조건이 코드에 있는지 확인하기
        func(idx+1, broken) # 치지 않고 넘어간다
        return

    for i in range(N):
        if i==idx or end[i]<=0: # 깨지지 않은 다른 계란
            continue
        end[i] -= wei[idx] #  중에서 하나를 친다
        end[idx] -= wei[i]

        cnt = broken
        if end[i]<=0: cnt += 1
        if end[idx]<=0: cnt += 1
        func(idx+1, cnt) #  한 칸 오른쪽 계란
        end[i] += wei[idx]
        end[idx] += wei[i]

func(0, 0) # 가장 왼쪽의 계란을 든다
print(rst)