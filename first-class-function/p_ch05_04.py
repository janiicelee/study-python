#decorator
#장점
#1. 중복제거, 코드간결, 공통함수 작성
#2. 로깅, 프레임워크, 유효성체크 -> 공통함수
#조합해서 사용하기 편하다

#단점
#1. 가독성 감소?
#2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
#3. 디버깅 불편

#데코레이터 실습

import time

def performance_clock(func):
    def perf_clocked(*args):
        #함수 시작 시간
        start_time = time.perf_counter()
        #함수 실행
        result = func(*args)
        #함수 종료시간
        end_time = time.perf_counter() - start_time
        #실행 함수명
        name = func.__name__
        #함수 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        #결과 출력
        print('[%0.5fs] %s(%s) -> %r ' % (end_time, name, arg_str, result))

        return result
    return perf_clocked


def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)


#데코레이터 미사용
none_deco1 = performance_clock(time_func)
none_deco2 = performance_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

#데코레이터 사용

@performance_clock
def time_func(seconds):
    time.sleep(seconds)

@performance_clock
def sum_func(*numbers):
    return sum(numbers)

