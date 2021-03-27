#tuple advanced
#unpacking

# b, a = a, b

print(divmod(100,9))
print(divmod(*(100,9)))
print(*divmod(100,9))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1,2,3,4,5
print(x, y, rest)

print()
print()


#mutable (가변) vs immutable (불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l*2
m = m*2
print(l, id(l))
print(m, id(m))

l*=2
m*=2
print(l, id(l))
print(m, id(m))

#tuple 은 계속 바뀜
#list는 자기자신의 아이디에 할당됨 

#
# sort vs sorted
# reverse, key = len, key=str.lower, key=func...

#sorted = 정렬 후 새로운 객체 반환 (원본은 그대로)
f_list = ['orange', 'apple', 'mango', 'lemon', 'coconut']

print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - 1', sorted(f_list, key=lambda x: x[-1]))
print('sorted - 1', sorted(f_list, key=lambda x: x[-1], reverse=True))
print(f_list)

#sort = 정렬 후 객체 직접 변경 (원본 변경)

print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)


#list vs array
#리스트 기반: 융통성, 다양한 자료형, 범용적 사용
#숫자 기반: 배열(리스트와 거의 호환)


