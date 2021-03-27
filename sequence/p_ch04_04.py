#시퀀스형
#해시테이블 -> 적은 리소스호 많은 데이터를 효율적으로 관리
#dict -> key 중복 허용 x, set -> 중복 허용 x
#dict , set심화

#immutable Dict
from types import MappingProxyType

dict = {'key1': 'value1'}

#read only
dict_frozen = MappingProxyType(dict)

print(dict, id(dict))
print(dict_frozen, id(dict_frozen))

#수정 가능
dict['key2'] = 'value2'
# dict_frozen['key'] = 'cant go in'
print(dict)
print(dict_frozen)

print()
print()

s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'}
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
s3 = {3}
s4 = set() # not {}
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'}) # read only

s1.add('melon')
print(s1)


# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행 
from dis import dis

print('-------')
print(dis('{10}')) #더빠름
print('-------')
print(dis('set([10])'))


#지능형 집합 comprehending set
print('------')
from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
