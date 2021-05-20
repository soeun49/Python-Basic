def bool_ex(): #bool 자료형
    print ("======bool 연습")
    #참(true), 거짓(false)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단
    #bool의 판정 방법
    print(bool(0), bool(1)) #bool(0): 비어있다--> 거짓, bool(1): 비어있지 않다--> 참
    a=1
    print (a>10) # 논리 연산 or 비교 연산의 결과

    b=a==1 # a==1인것이 맞는지 판단 -> b가 boolean type이 됨
    print (b,type(b))

    print (b+10)

    #bool은 bool의 객체인가?
    print(isinstance(True, bool)) # True is boolean?
    print(isinstance(True,int)) # true is int?

    #bool 캐스팅
    print("정수형:", bool(10), bool(0))
    print("실수형:", bool(3.14), bool(0.0))
    print("문자열:", bool("Python"), bool(""))
    print("순차형:", bool([1,2,3]),bool([]))
    print("Map:", bool({"a":2}), bool({}))
    print("None:", bool(None)) # None: Java의 NULL과 비슷 --> 아무 것도 할당되어 있지 않은 상태를 의미
    

if __name__=="__main__":
    bool_ex()