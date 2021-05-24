def handling_exception():
    """
    예외 처리하기
    """

    lst=[]
    #1번째 예외처리

    try:
        lst[3]=1
        4/0
        int("String")
    except Exception:
        print("Error")

    #예외 회피는 가능하지만 실제로 어떤 오류인지, 어떻게 회피해야 하는지 확인이 불가능함

    #2.
    try:
        # lst[3]=1
        # 4/0
        # int("String")
        print(int("123456789"))
    except ValueError as e:
        print("정수로 변환 불가!")
        print(e,type(e))
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없습니다.")
        print(e,type(e))
    except IndexError as e: #구체적인 예외처리가 가능해짐
        print("인덱스에 접근할 수 없습니다.")
        print(e,type(e))
    except Exception as e: #예외 객체의 심볼을 붙이면 어떤 예외인지 확인 가능
        print("Error")
        print(e,type (e)) # IndexError임을 확인 가능해짐
    else: #try블록에서 예외가 없을 때 한번 실행함
        print("예외 없음")
    finally: #예외 유무 관계없이 항상 마지막에 -> 주로 자원 정리에 사용됨
        print("예외 처리 종료")

    #예외 있을 때: try -> except-> finally
    #예외 없을 때: try -> else -> finally

def raise_exception():
    """
    예외의 위임
    """
    def beware_dog(animal): #animal== "dog" --> 예외 발생, else: "어서오세요!"
        if animal == "dog": #예외를 외부로 위임
            raise RuntimeError("강아지는 출입을 제한합니다.")
        else:
            print(animal, "어서오세요.")

    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e,type(e))
        
    print ("End of Code")
if __name__=="__main__":
    # handling_exception()
    raise_exception()