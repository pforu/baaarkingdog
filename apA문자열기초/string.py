s = " ,.Life is is short, y@@ #eed PPPPPPython.!"

start = s.find('is') # 인덱스 반환, 없으면 -1
s.find('is', start+1) # 어디서 시작할지 설정가능 
s.rfind('is') # 뒤부터 찾음 
s.count('PP', s.find('P')+1) # 2, 중복되지 않게 찾음, 어디서 시작할지 설정가능 
replaced = s.replace('-', ':') # 모두 찾아서 바꿈, 재할당 필요, 최대 몇 개 바꿀지 설정가능 

s.startswith("pre")
s.endswith("suf")
# 대체로 찾을 부분, 즉 시작하고 끝나는 지점 설정가능
s.removeprefix("pre")
s.removesuffix("suf")

s = s.upper()
s = s.lower()
s = s.capitalize() # I love python
s = s.swapcase() # i LOVE PYTHON

s.isalpha()
s.isdecimal()

filtered = "".join(c for c in s if c.isalnum()) # 알파벳과 숫자만 남기기
clean = s.strip(" ,.!") # 양 끝의 특정문자를 제거 
s.split(':')

num = 1234567890
print(f"{num:,}")

import re
# \d: 숫자 = [0-9]
# \D: not 숫자
# \w: 문자, 숫자, 언더바 = [a-zA-Z0-9_]
# +: 1개 이상 반복
# *: 0개 이상 반복
# []: 안의 문자 중 하나

text = "전화: 010-1234-5678, 가격: 50,000원"
numbers = re.findall(r'\d+', text) # 1개이상의 연속숫자 찾기 -> 리스트
cleantext = re.sub(r'\D', '', text) # 숫자가 아닌 것을 없애기 -> 문자열 
parts = re.split(r'[,:]', text) # 여러 구분자로 자르기 -> 리스트 
