def using_range():
    # range 객체: 범위 생성
    #인자가 1개: 0부터 인자경계 이전까지
    #실제 값은 가지고 있지 않고, 필요할 때 한개씩 생성

    seq= range(10) # 0~9
    print(seq,type(seq))
    print(list(seq))

    #인자가 2개: 시작 경계, 끝 경계
    seq2 = range(2,10) #2~9
    print(seq2)
    print(list(seq2))

    #인자가 3개: 시작경계, 끝경계, 증감값
    seq3=range(2,10,2) #2~9까지 2씩 증가
    print (seq3)
    print(list(seq3))

    #증감값이 음수: 큰숫자 -> 작은 숫자
    seq4=range(0,-10,-1) #0이하, -10초과 역순 정수
    print(seq4)
    print(list(seq4))

    #실제 값은 가지고 있지 않지만
    #순차 객체 이므로: 길이 확인, 포함 여부 확인 가능
    print(seq, "LENGTH:", len(seq))
    print (5 in seq)

    #인덱스를 이용, 내부 데이터 접근 가능
    print(seq[0], seq[1], seq[2])
    print(seq[-1],seq[-2],seq[-3])

    #슬라이싱 가능
    print(seq[2:5])

    #but 불변객체이고, 실제 데이터 값을 가지고 있지 않으므로
    #인덱스, 슬라이싱을 이용한 치환은 불가능하다

    #range객체를 이용한 for 루프 예제
    for i in range(10): #시작 0, 끝 9, 간격 1
        print(i, end=" ")
    else:
        print()

def using_enumerate():
    """
    enumerate 함수: 순차형에서 현재 아이템과 함께 내부 인덱스도 함께 필요할 때 사용
    """
    colors = ["red", "yellow", "blue", "white", "grey"]
    i=0
    for color in colors: #항목 값은 확인할 수 있지만, 인덱스는 확인 불가
        print("COLOR {0}:{1}".format(i,color))
        i+=1

    print ("===========enumerate")
    for item in enumerate(colors): #튜플로 반환 (index, 항목)
        print(item)

    for index,color in enumerate(colors): #(index,항목) -> unpacking
        print("COLOR {}: {}".format(index,color))

def using_zip():
    #zip 객체: 여러 개의 순차자료형을 동시에 루프시키는 객체

    english= "Sun", "Mon", "Tue", "Wed"
    korean = "일요일","월요일","화요일","수요일","목요일"
    engkor=zip(english,korean) #묶이는 조합의 길이는 짧은 쪽으로 맞춰짐
    print (engkor, type(engkor))

    #기본 순회
    for pair in engkor: # 조합의 튜플 반환
        print(pair, type(pair))

    #zip객체는 일회성 객체 -> 루프를 돌면 비워짐
    engkor=zip(english, korean)

    #Unpacking 순회
    for eng,kor in engkor: #조합의 튜플 -> unpacking
        print(eng, "->", kor)

    engkor=zip(english,korean)
    #인덱스, 영어, 한국어

    for index,(eng,kor) in enumerate(engkor):
        print(index,eng, kor)

    #zip객체를 이용 -> 사전 생성
    print(dict(zip(english,korean)))

if __name__=="__main__":
    # using_range()
    # using_enumerate()
    using_zip()
