import sys
input = sys.stdin.read

arr = input().split()[1:]
for i in range(len(arr)):
    tmp = list(arr[i])
    tmp.reverse() # list 함수 
    arr[i] = int(''.join(tmp)) # list->str : join 사용 

arr.sort()
print(*arr, sep='\n')