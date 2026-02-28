import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
st = []
orda = ord('A')
for alp in zip(A, B):
    for i in alp:
        st.append(alpha[ord(i)-orda])

while True:
    if len(st)==2:
        break
    tmp = []
    for two in zip(st[:-1], st[1:]):
        tmp.append(sum(two) % 10)
    st = tmp[:]

print(''.join(map(str, st)))