import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1)
d[1] = 0
for i in range(2, n+1):
    arr = []
    if i%3==0:
        arr.append(d[i//3])
    if i%2==0:
        arr.append(d[i//2])
    arr.append(d[i-1])
    d[i] = min(arr)+1
print(d[n])

# 배열에 담지 말고, 그때그때 최솟값 갱신 가능 