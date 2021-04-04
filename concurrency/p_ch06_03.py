# 코루틴: 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업 
# 쓰레드 : os관리, cpu코어에서 실시간 시분할 비동기 작업 -> 멀티쓰레드 
# yield, send: 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송 

# 서브루틴: 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴: 루틴 실행 중에 중지 -> 동시성 프로그래밍
# 코루틴의 장점: 쓰레드에 비해 오버헤드 감소
# 쓰레드: 싱글쓰레드 -> 멀티 쓰레드 -> 코딩 복잡 -> 공유되는 자원 -> 교착상태 발생가능성, 컨텍스트 스위칭 비용발생, 자원 소비 가능성증가

#def -> async, yield -> await

#코루틴 ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine recieved : {}'.format(i))

# 제너레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

next(cr1)

# cr1.send()

# 코루틴 ex2

# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPENDED: yield 대기 상태
# GEN_CLOSED: 실행완료 상태

def coroutine2(x):
    print('>>> coroutined stated: {}'.format(x))
    y = yield x
    print('>>> coroutined received: {}'.format(y))
    z = yield x + y
    print('>>> coroutined received: {}'.format(z))

cr3 = coroutine2(10)
print(next(cr3))
cr3.send(100)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))
# print(next(cr3))
# cr3.send(100)


#코루틴 ex3
#stopiteration 자동처리(3.5->await)
#중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x

    for y in range(1, 4):
        yield y

t1 = generator1()

print(next(t1))


t2=generator1()
print(list(t2))

print()
print()

def generator2():
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()

print(next(t3))
print(next(t3))

print()
print()