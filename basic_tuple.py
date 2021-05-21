def define_tuple():
    """
    튜플 정의 연습
    """
    tp=tuple()
    print(tp,type(tp))

    #캐스팅: 다른순차자료혀을 기반으로 튜플생성
    tp=tuple({1,3,5,7,9})
    print(tp,type(tp))

    tp=() #공튜플
    tp2=(1,) #요소의 갯수가 한 개일때에는 반드시 콤마를 추가
    tp3=(1,2,3)

    print(tp,tp2,tp3)

def tuple_oper():
    """
    튜플의 연산
        대부분 리스트와 비슷: len, indexing, slicing, in or not in
        immutable 자료형
            슬라이싱을 이용한 치환은 불가(!)
            메서드는 한정적
    """
    tp=(1,2,3,4,5)
    #길이를 구할 수 있다
    print(tp,"LENGTH:", len(tp))
    #인덱스 접근이 가능
    print(tp[0],tp[1], tp[2], tp[3],tp[4]) #정인덱싱
    print(tp[-5],tp[-4],tp[-3],tp[-2],tp[-1]) #역인덱싱

    # tp[3]=0 :TypeError -> immutable

    #연결, 반복, 포함여부 확인 등은 모두 list와 동일

def tuple_methods ():
    #메서드가 많지 않다
    tp=(20,30,10,20)
    #검색: index
    print("1st 20:",tp.index(20))
    print("2nd 20:", tp.index(20,1)) #검색 범위의 제한

    #갯수 확인
    print("COUNT of 20:", tp.count(20))

def packing_unpacking():
    """
    튜플의 패킹 &언패킹
    """
    tp=(10,20,30,"Python")
    print(tp,type(tp))
    tp1 = 10, 20, 30, "Python" #()로 명시하지 않아도 튜프롤 인식
    print(tp1,type(tp1))

    #기본 Unpacking
    (a,b,c,d)=tp
    print(a,b,c,d)
    #일반적으로
    a,b,c,d=tp
    print(a,b,c,d)

    # a,b,c=tp ->변수의 갯수가 맞지 않으면 ValueError(!)
    # a,b,c,d,e=tp -> ValueError(!)

    #확장 언패킹
    #지정되지 않은 개수의 요소 변수 앞에 *
    a,*b =tp
    print(a,b)

    *a,b=tp
    print(a,b)

    a,*b,c = tp
    print(a,b,c)


if __name__ =="__main__":
    # define_tuple()
    # tuple_oper()
    # tuple_methods()
    packing_unpacking()