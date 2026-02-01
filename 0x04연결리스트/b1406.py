import sys
input = sys.stdin.readline

#파이썬에서 원형 연결리스트가 필요하다면 deque.rotate() or %연산 

MX = 600005
data, pre, nxt = [None]*MX, [-1]*MX, [-1]*MX
unused = 1 ### 0번은 더미 

def insert(addr, val): #addr은 주소이나, 파이썬이므로 idx 의미 
    # addr의 주소를 가진 노드의 다음에 val값을 가진 노드 추가 
    global unused ### 함수 쓸 때 항상 주의 
    data[unused] = val #2번의 데이터 = val
    pre[unused] = addr #2번의 전 노드 = 1 
    nxt[unused] = nxt[addr] #2번의 다음 노드 = 1번의 다음 노드 = 3번 
    if nxt[addr] != -1: #3번이 있었다면 
        pre[nxt[addr]] = unused #3번의 전 노드 = 2번 
    nxt[addr] = unused #1번의 다음 노드 = 2번 
    unused += 1

def erase(addr):
    nxt[pre[addr]] = nxt[addr] #1번의 다음 노드 = 2번의 다음 노드 = 3번 
    if nxt[addr] != -1: #2번의 다음 노드가 있다면
        pre[nxt[addr]] = pre[addr] #3번의 전 노드 = 2번의 전 노드 = 1번 

def traverse():
    cur = nxt[0] #더미(0) 다음부터 출력 
    tra = []
    while cur != -1:
        tra.append(data[cur])
        cur = nxt[cur]
    print("".join(tra)) ### 리스트 출력 시 항상 형식 지정 생각하기 


ed = list(input().strip()) ### 수정이 필요할 경우는 리스트 변환, 아닐 경우 문자열 사용 무방
cursor = 0
for val in ed:
    insert(cursor, val)
    cursor = nxt[cursor]

N = int(input())
for i in range(N):
    ins = input().strip().split() ### split()은 앞뒤와 사이의 모든 공백을 지움, strip 필요 없음 
    ### 단일 데이터 혹은 한 줄을 읽을 때는 필수 
    match ins[0]:
        case 'L':
            if pre[cursor]!=-1: # cursor>= 0
                cursor = pre[cursor] ### +-1이 아니라 따라가기 
        case 'D':
            if nxt[cursor]!=-1: # cursor<= unused-1
                cursor = nxt[cursor]
        case 'B':
            if pre[cursor]!=-1:
                erase(cursor)
                cursor = pre[cursor] ### 지우거나 삽입 후 전/다음으로 커서 이동 
        case 'P':
            insert(cursor, ins[1])
            cursor = nxt[cursor]

traverse()
