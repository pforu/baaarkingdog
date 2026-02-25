import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

d = [0]*(K+1)
d[0] = 1 # i-c==0일 때, 즉 값이 n인 동전으로 n원을 만들 때 가짓수 1, 초기값설정 

for c in coin:
    for i in range(c, K+1):
        d[i] += d[i-c]

# print(d)
print(d[K])

### 동전이 바깥쪽 루프인 건, 동전을 하나씩 시장에 출시하는 것
# 모든 금액(i)을 만드는 방법은 1원으로만 채우는 경우 딱 1가지씩뿐
# 기존에 1원으로만 만들었던 방법들에 2원짜리를 섞는 방법을 새로 추가
# 이미 1원 조사가 끝난 상태에서 2원을 얹기 때문에
# 2원 뒤에 1원이 오는 경우는 따로 세지 않음
# 즉 조합이 됨 

# 원래는 금액을 바깥 루프로 했음, 이건 2+1과 1+2를 다르게 세는 순열의 방법 
# 동전이 바깥쪽 루프면: "동전 A를 다 쓰고 나서 동전 B를 고려하자" → 순서가 고정됨 (조합)
# 금액이 바깥쪽 루프면: "이번 금액을 만들 때 모든 동전을 다 써보자" → 순서가 뒤섞임 (순열)



# 순열조합으로 하면 바로 시간초과 
# div = []
# for c in coin:
#     div.append(range(K//c + 1))

# rst = 0
# for p in product(*div):
#     sumval = 0
#     for i, cnt in enumerate(p):
#         sumval += coin[i] * cnt
#     if sumval==K:
#         rst += 1
# print(rst)