def bool_ex(): #bool 자료형
    """
    boolean 자료형 연습
    isinstance()
    esp., circuit break
    or : 순서 상 먼저 나온 True 값을 반환
    and:
    1) True1&True2: 순서 상 나중에 나온 True2값을 반환
    2) True&False: False 값을 반환
    """
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

    #Circuit Break
    print("CB or 1:", [1,2,3] or [])
    #or: True or False --> 먼저 나온 True 반환 : 기본값 설정시 쓰는 방법
    print("CB or 2:", [] or [1,2,3])
    #False or True: 먼저나온 True 값인 (순서 상) [1,2,3]반환
    print("CB and 1:", [1,2,3] and [4,5,6])
    #cf. AND: 뒤의 값을 반환 (True&True -> T2 반환)
    print("CB and 2:", [1,2,3] and [])
    #True & False: False의 값을 반환 --> [] (=none) 값을 반환


def integer_ex():  #정수형
    """
    정수형 연습 (integer)
    in Python: only int (cf. in Java: int, long)
    2진:0b (b for binary); bin()
    8진:0o (o for oct); oct()
    16진:0x (x for hex); hex()

    """
    print("==========정수형 연습")
    a=23 #Literal
    b=int(23) #타입 함수를 이용
    print(a,"is",type(a))
    print(b,"는 int의 객체?", isinstance(b,int))

    #2진, 8진, 16진 정수 표현 가능
    b= 0b1101 #2진: 0b
    o=0o23  #8진: 0o
    x=0xFF #16진: 0x
    print(b,o,x)

    #3.x에서는 int, long을 구분하지 않음
    #long형의 저장크기인 64bit를 초과하는 정수도 입력 가능
    i=2**2048
    print(i)
    print(i.bit_length()) #i 객체의 비트수 확인

    #진법 변환 함수
    print(bin(2021))
    print(oct(2021))
    print(hex(2021))

def float_ex(): #실수형은 모두 float로 표기
    """
    실수형 연습 (float)
    in Python: only float (cf. in Java: float, double)
    e or E -> expressing float
    """
    print("==========실수형 연습")
    a=3.14159 #리터럴로 선언
    print(a,"is", type(a))
    b=float(3.0) #타입 함수를 이용한 생성
    print (b, "는 float의 객체인가?", isinstance(b,float))
    #is_integer: 타입 판별이 아니라 값의 형태가 정수형(소숫점 아래 값이 없는지) 인지를 판별
    print(a.is_integer(), b.is_integer())

    #소수점 포함, e,E 지수 형태로 표현 가능
    c=3e3 #3000
    d=-2E-5 #-0.00002
    print(c,d)
    print(-2E-5==-0.00002)

def complex_ex():
    """
    복소수 연습 (Complex Number:i)
    in Python: can express Complex Number (cf. in Java: x)
    j or J -> expressing complex
    .real, .imag, .conjugate
    """
    #복소수
    print("=====복소수 연습")
    # 복소수: 실수부 + 허수부J 형태
    a=4+5j # 실수부 4, 허수부 5
    print(a,"is",type(a))
    b=7-2J #실수부 7, 허수부 -2
    print(b, "complex의 객체?", isinstance(b,complex))

    #복소수는 수치형 --> 산술연산 가능
    print (a+b)

    print(a,"의 실수부?", a.real)
    print(a,"의 허수부?", a.imag)
    print(a, "의 켤레 복소수?", a.conjugate())

    #타입 함수를 이용한 복소수의 생성
    c=7
    d=3
    e=complex(7,3)
    print(e, "is", type(e))

def builtin_math_function(): #내장 수치 함수
    """
    내장 수치 함수(builtin mathematical function)
    함수를 통해서 숫자를 출력할 수 있음
    """
    print(abs(-1)) #절댓값
    print(int(3.14159)) #타입 함수를 이용한 타입의 변환
    print(float(3)) #타입변환
    print(complex(1)) # 타입변환
    print(divmod(5,3)) #정수 나눗셈 (몫, 나머지)
    print(pow(2,10))

if __name__=="__main__":
#    bool_ex()
#    integer_ex()
#    float_ex()
#    complex_ex()
    builtin_math_function()