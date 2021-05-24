#함수 스코핑 룰
x=1 #global

def scope_func(a):
    return a+x #local scope에 x가 없음 -> 글로벌 x를 참조함

def scope_func2(a):
    x=2 #치환 -> local scope에 x심볼이 생성 -> 글로벌 x가 아님
    return a+x # local scope a, local scope x 합산 return

print(scope_func(10))
print(scope_func2(10))
print("global x:",x) #scope_func2에서 x가 치환되었지만 global x는 변경되지 않음

g=1

def scope_func3(a):
    g=3
    return a+g

print(scope_func3(10))
print("global g:",g)