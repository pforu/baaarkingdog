s1 = set()
s2 = set()
val = 4
key = 'name'
c1 = Counter()
c2 = Counter()

### set
s = set()
s.add(val)
s.remove(val) # 없으면 에러
s.discard(val) # 없어도 됨 None 반환
val in s
s1 | s2, s1 & s2, s1 - s2


### dictionary
d = {}, d = dict()
d['name'] = 'kim'
d.pop(key, None) # 없으면 None 반환 
d.get(key, None) # d[key]보다 안전 
key in d
d.keys(), d.values(), d.items()

for key in d: # 키 순회
    pass
sorted_dict = sorted(d.items(), key= lambda x: x[1]) # value 기준 정렬 

from collections import defaultdict
d = defaultdict(int) # 기본값 100 - d = defaultdict(lambda: 100)
d['no_key'] += 1


### collections.Counter
from collections import Counter
arr = ['apple', 'banana', 'apple']
count = Counter(arr)
count['apple']
count.most_common(2) # 인자 없을 시 전체 빈도순 정렬 
c1 + c2, c1 - c2
list(count.elements())