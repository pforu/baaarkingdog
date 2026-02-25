import sys
input = sys.stdin.readline

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))

time = 0
idx = 0
brid = [0]*W
while True:
    if idx==N and sum(brid)==0:
        break
    elif idx<N and sum(brid[1:])+truck[idx] <= L:
        # 하나가 나가면서 들어오는 건 무게제한 포함이 아니므로 brid[1:]로
        brid = brid[1:] + [truck[idx]]
        idx += 1
    else:
        brid = brid[1:] + [0]
    time += 1
print(time)