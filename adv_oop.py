class MyString(str): # str클래스를 상속 받은 MyString
    pass #MyString은 str 클래스에서 모든 멤버들을 물려 받는다

s=MyString() #인스턴스 생성
print (type(s)) #타입의 확인
print(MyString.__bases__) #기반(부모) 클래스의 확인
#(<class 'str>,) -> 튜플; 여러개의 클래스를 상속받을 수 있음을 보여줌
# 파이썬은 중복상속/다중상속이 가능함

print(str.__bases__) #모든 클래스의 최상위 클래스: object

class myobj:
    pass

class Chimera(str,myobj):
    pass

print("type:",type(Chimera))
print(Chimera.__bases__)

# 하위 클래스 or 파생 클래스 확인: issubclass()
print("Chimera는 str의 서브클래스?", issubclass(Chimera,str))
print("Chimera는 myobj의 서브클래스?", issubclass(Chimera,myobj))

# 상위 클래스 or 기반 클래스 확인: 별도 함수 없음, __bases__ 사용


#Mystring 은 str을 상속 -> str의 모든 멤버를 상속
ms= MyString("Python")
print(ms)
print(dir(ms))
#str의 모든 메서드를 그대로 활용
print(ms.upper())


