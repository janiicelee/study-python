#외부에서 호출된 함수의 변수값, 상태 복사 후 저장 -> 후에 접근 가능 

# closure 사용

def closure_ex1():
    # free variable
    #클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {}/{}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager

avg_closure1 = closure_ex1()
print(avg_closure1(10))


print()
print()

#function inspection

print(dir(avg_closure1))
print()
print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)

print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()

#잘못된 클로저 사용 예시
def closure_ex2():
    #free var
    cnt=0
    total=0
    def averager(v):
        cnt += 1
        total += v

        return total / cnt 
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) 예외 


def closure_ex3():
    #free var
    cnt=0
    total=0
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v

        return total / cnt 
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10)) 
