# 연산자 연습
def arith_oper(): #산술 연산자 연습
    """
    기본 산술 연산자 (Basic Arithmetics Operator)
    """
    print ("===============산술연산")
    #+,-,* /
    print (7/3) #정수와 정수를 나눠도 실수 형태로 표현
    print(6/2)

    #//: 정수 나눗셈의 몫 연산자
    print(7//3)  #정수 나눗셈의 몫
    print(7%3)  #정수 나눗셈의 나머지

    #divmod 함수: 몫과 나머지를 동시에 구하는 방법
    print(divmod(7,3)) #7을 3으로 나눈 몫과 나머지 (몫, 나머지)
    print(divmod(7,3)[0])
    print (divmod(7,3)[1])

    #제곱 연산자: **
    print (7**3)
    print(pow(7,3)) # 내장 수치 제곱 함수

def complex_ex():
    """
    복소수(Complex Number)
    """
    print ("===============복소수")
    print (3+4j) #실수부 +허수부 + j
    print ((3+4j).real) #실수부 반환
    print ((3+4j).imag) #허수부 반환
    print((3+4j).conjugate()) #켤레 복소수

    print(complex(3,4)) #타입 함수를 이용한 복소수 선언


def rel_oper(): # 비교 연산자 연습
    """
    비교 연산자 (Comparison Operator)
    """
    print("===============비교 연산(관계 연산)")
    print ("1>3 ?", 1 >3)
    print ("1<3 ?", 1<3)
    print ("6 equals 9 ?", 6 ==9)
    print("6 not equals 9 ?", 6 !=9)

    s1="Python"
    s2="Python"

    print ("문자열의 ==", s1==s2)

    #복합 관계식
    a=6
    #a가 0보다 크고 10보다 작은가?
    print(a > 0 and a<10)
    print(0<a and a<10)
    print(0 < a < 10)

    #수치형 이외 다른 타입의 객체 비교
    print("문자열의 대소:", "abcd">"abd")
    print("튜플의 대소:", (1,2,4) >(1,3,1))
    print ("리스트의 대소:", [1,2,4] <[1,3,1])

    #동질성의 비교: == ; 동일성의 비교: is
    #is 는 객체 항목에서 더 자세하게 학습할 예정

    a=10
    b=20
    c=a
    print("a==b?", a==b)
    print("a is b?", a is b)
    print("a==c?", a==c)
    print("a is c?", a is c)



def variable_ex(): #변수
    """
    변수 지정 (Defining Variables)
    """
    print("=======변수")
    #변수 명은 문자, 숫자, _의 조합
    #숫자로 시작하면 안됨
    #예약어는 사용 불가능
    import keyword # keyword 모듈 로드
    print(keyword.kwlist)
    print("키워드 갯수:", len(keyword.kwlist))

    #UNICODE 이름의 변수도 사용 가능 -> 권장 x
    가격 = 12000
    print (가격 + 가격*0.1)

def assignment_ex(): #치환문
    """
    치환 (Substitution/Replacement)
    """
    print("======치환문")

    #여러 변수를 한꺼번에 할당
    a,b = 3.5, 5.3 #좌변의 변수의 갯수와 우변의 값의 갯수가 일치해야 함
    print (a,b)

    #값 교환
    a,b=b,a
    print(a,b)
    # 이 방식을 이용해 함수의 return값을 생성 가능함

    #같은 값을 여러 변수에 동시 할당
    x=y=z=2021
    print(x,y,z)

    # 중요: 동적 타이핑 (dynamic: 값의 할당시, 데이터 타입에 제한이 없음)
    # 파이썬은 변수 선언이 없음, 그리고 값이 할당될 때 데이터 타입이 결정
    a=1
    print (a, "is", type(a)) # type함수 -> 데이터 혹은 객체의 데이터 타입을 확인
    a= "Hello Python" # 동적 타이핑!
    print (a, "is", type (a))

    # isinstance(판별할 값 or 객체, 데이터 타입)
    print("a는 str의 객체?", isinstance(a,str))


def logical_oper(): # 논리 연산자
    """
    논리 연산자 (Logical Operator)
    논리곱 (and), 논리합(or), 논리부정(not)
    """
    print (("=====논리연산 "))

    #논리곱 (and): 둘 다 true일때 true
    #논리합 (or): 둘 중 하나면 true이면 true
    #논리부정 (not): true <-> false

    a,b=20,30
    print (not a<b) #a<b의 논리를 부정
    print(a<b and a!=b) #a<b 의 논리값과 a!=b의 논리값의 논리곱
    print(a==b or a!=b) #a==b의 논리값과 a!=b의 논리값의 논리합

def bit_oper(): #비트 연산자: int 데이터를 비트 단위로 정밀하게 제어
    """
    비트 연산자 (Bit Operator)
    bin() -> 10진수 숫자를 2진수 숫자로 변경 (decimal to binary)

    """
    print("=====비트 연산자")
    #비트 NOT : 1>>>>>>0
    print (bin(5),bin(~5))  #~: bit not 이진수 보수 표기법

    #비트 시프트: << (좌측으로 이동), >> (우측으로 이동)
    bits=1
    print(bin(bits))
    bits=bits<<4 #왼쪽으로 4비트 이동
    print(bin(bits))

    bits = 0b10101010
    print(bin(bits))
    print(bin(bits & 0b10))  # bit and
    print(bin(bits | 0b1111))  # bit or

if __name__=="__main__":  #main logic 수행
#    arith_oper()
#    complex_ex()
#    rel_oper()
#    variable_ex()
#    assignment_ex()
#    logical_oper()
    bit_oper()