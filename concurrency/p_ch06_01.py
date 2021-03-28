#병행성 Concurrency
#iterator, generator

#파이썬 반복가능한 타입
#collections, text file, list, dict, set, tuple, unpacking, *args

#while
t = 'abcde'

from collections import abc

print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

#next
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')

        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop Iteration. ')
        
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print()
print()

# generator 

# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이처 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용 

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word #generator 
        return 

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('i want mango')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()