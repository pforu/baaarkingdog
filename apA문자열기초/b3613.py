import sys
input = sys.stdin.readline
# _가 맨 앞, 맨 뒤, 혹은 연속으로 두 번(__) 쓰였는지 고려하지 않음 
inp = input().strip()
rst = 0
error = False

if inp.islower():
    c_word = []

    for i, c in enumerate(inp.split('_')):
        if c=='':
            error = True
            break

        ad = c.capitalize()
        if i==0: 
            ad = c
        c_word.append(ad)

    rst = ''.join(c_word)

else:
    j_word = []

    for i, j in enumerate(inp):
        if j=='_' or (i==0 and j.isupper()):
            error = True
            break

        ad = j
        if j.isupper():
            ad = '_' + j.lower()
        j_word.append(ad)

    rst = ''.join(j_word)

if error:
    rst = 'Error!'
print(rst)