#클로저 사용이유
#서버 프로그래밍 -> 동시성 제어  -> 메모리 공간에 여러자원이 접근 -> 교착상태 (dead lock)
#메모리를 공유하지 않고 메세지 전달로 처리하기 위한 -> Erlang
#클로저는 공유하되 변경되지 않는 (immutable, read-only) 적극적으로 사용 -> 함수형 프로그래밍
#클로저는 불변 자료구조 및 atom, STM -> 멀티스레드Coroutine 프로그래밍에 강점 

a = 100
print(a+100)
print(a+1000)

print(sum(range(1,51)))

#클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {}/{}'.format(self._series, len(self._series)))
        return sum(self._series) /len(self._series)

#인스턴스 생성
averager_cls = Averager()

#누적
print(averager_cls(10))
print(averager_cls(30))
