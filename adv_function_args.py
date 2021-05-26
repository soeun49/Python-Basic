#함수의 인수는 필요한 개수만큼 선언가능함
def sum_val(a,b): #a,b=고정인수
    return a+b

def incr(a,step=1): #2번째 인자값은 기본값
    return a+step

print (sum_val(2,3)) #고정인수를 전달할때에는 순서대로(!)
print(incr(10)) #기본값이 있는 인수는 전달하지 않으면 기본값이 선택됨
print(incr(10,2)) # 기본값이 아닌 전달된 인수값이 선택됨

#키워드 인수
#인수의 값을 인수의 이름으로 전달 -> 인수의 순서는 바뀌어도 상관없음

def area(width, height):
    print("width:", width)
    print("height:", height)
    return width*height

print(area(10,12)) #인수 이름 명시 안함 -> 선언 순서대로 전달함
print(area(height=12, width =10)) #인수 이름을 명시하면 인수의 순서와는 상관없이 선언됨

#가변인수: 정해지지 않은 갯수의 인수를 받을 때
#인수명 앞에 *를 붙여 선언한다
def get_total(*args): #여러 개의 인수를 전달받아서 합산 후 return
    total=0
    print("인수:",args, type(args))
    for x in args:
        total +=x
    return total

print(get_total(1,3,5,7,9))


#응용
#1.가변인수로 값을 넘긴다
#2.넘겨받은 인수가 int 혹은 float인경우, 합산
#3. list, tuple일 경우 내부 루프 돌면서 합산
#4. 나머지는 합산하지 않음
#5. 재귀 x

def get_total2(*args):
    total=0
    for x in args:
        if isinstance(x,(int,float)): #인수값이 int or float
            total+= x
        elif isinstance(x,(list,tuple)): #인수가 list or tuple
            for item in x:
                if isinstance(item,(int,float)):
                    total+=item
    return total

print(get_total2(1,2,3,4,5))
print(get_total2(1,2,"3",4,5))
print(get_total2(1,2,[3,4,5]))

#사전 키워드
#지정되지 않은 키워드들 -> dict로 변환되서 사전 키워드로 전달
#사전 키워드 인수 앞에 **를 붙인다

def args_test(a,b,*args,**kwd):
    #a,b -> 고정 인수
    #args -> 가변인수
    #kwd -> 사전 키워드 인수
    print("고정인수:",a,b)
    print("가변인수:",args)
    print("사전키워드:",kwd)

#인수의 순서가 중요; 고정인수-> 가변인수-> 사전키워드 순으로 선언!
args_test(10,20,30,40,50,option1="value1", option2="value2")


#함수도 객체: 함수도 변수에 참조 할당 되거나, 다른 함수의 인수로 전달될 수 있음
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def calculator(a,b,func): #a,b 는 숫자, func-> 함수
    if (callable(func)): #넘어온 인수 func가 실행 가능 객체인가?
        return func(a,b)

print(calculator(1,2,plus)) #합산 함수를 외부에서 전달
print(calculator(3,2,minus))

dirty_strings= "python pRogRamming, jaVa ProGrAMMING, LINUX , WinDows".split(",")
print(dirty_strings)

def clean_strings(strings,*funcs):
    results=[]
    for string in strings:
        # print(string)
        for func in funcs:
            if callable(func): #넘어온 인자가 실행 가능 객체인가?
                string =func(string)
        results.append(string)
    return results

cleaned= clean_strings(dirty_strings, str.strip, str.title)
print("CLEANED:", cleaned)


#__name__속성
# import 될 때 -> 자신의 이름
# 직접 실행될때 -> __main__

print("__name__:", __name__)
# 직접 실행되어서 __main__으로 나옴

if __name__ == "__main__":
    print("최상위 모듈로 실행되었습니다.")
else:
    print("import된 모듈입니다.")