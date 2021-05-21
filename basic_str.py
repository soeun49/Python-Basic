def define_str(): #문자열의 정의
    """
    문자열의 정의
    한 줄 문자열, 여러줄 문자열
    """
    #한 줄 문자열의 정의
    s1= "Hello Python" # 쌍따옴표("), 홑따옴표(') 모두 가능
    s2=str("Hello Python") # 타입 함수 이용 생성
    s3=str(3.14159) #타 타입을 문자열로 변환

    print(s1,s2,s3)
    print(type(s1), type(s2), type(s3))

    print("s1은 str의 객체?", isinstance(s1,str))

    #여러 줄 문자열의 정의: 쌍따옴표("), 홑따옴표(') x3 사이를 한 문자열로 판단
    s4=""" Life is too short, you need Python.
    파이썬은 데이터 처리가 중요한 시대에서 
    가장 널리 사용되는 언어이다    
    """

    print(s4) #Enter까지 포함되서 출력되는 것이 확인 가능

    #여러줄 문자열은 한줄 주석만 있는 파이썬에서
    #여러줄 주석을 사용하고자 할때 사용 가능하다.
    #메서드 정의부 바로 아래 여러 줄 문자열을 입력하면
    #help 명령어를 이용해서 해당 메서드의 주석을 볼 수 있다.
    #->docstring



def string_oper(): #문자열 연산
    #python console에서 파일(모듈)을 불러오기
    #import 파일명
    #help(파일명)
    """
    문자열 연산 연습
        str: len () -> 길이 확인
            연결 (+), 반복(*), 포함여부 확인 (in/not in) 가능
            인덱싱, 슬라이싱 가능
            immutable -> 내부 데이터 변경이 불가

    """
    str1 ="Python"
    # str2="Second String"

    #길이: len
    print("str1 length:", len(str1))

    #변경 불가 자료형 (immutable)
    # str1[0]='p'
    # str object does not support item assignment --> ERROR(!) 변경 불가 자료형이기 때문에 변경 불가

    #인덱싱: 배열과 비슷하게 인덱스로 접근
    #범위: 0~len()-1
    print("정인덱싱:", str1[0], str1[1], str1[2], str1[3],str1[4],str1[5])
    print("역인덱싱:", str1[-6],str1[-5],str1[-4],str1[-3],str1[-2],str1[-1])


    #슬라이싱: 경계범위 설정에 유의(!)
    print("[2:4] 슬라이싱:", str1[2:4]) #[시작 경계:끝 경계]
    print("[-4:-2] 슬라이싱:", str1[-4:-2]) #역인덱싱을 이용한 슬라이싱
    print("[0:3] 슬라이싱:", str1[0:3]) #처음부터 3번 인덱스까지 슬라이싱
    print("[:3] 슬라이싱:", str1[:3]) #시작 경계를 생략 -> 처음부터 3번인덱스까지
    print("[3:len(str1)] 슬라이싱",str1[3:len(str1)])
    print("[3:]슬라이싱:", str1[3:]) # 끝 경계를 생략 -> 3번 인덱스부터 끝까지
    print("[:] 슬라이싱:", str1[:]) #전체 복제

    #슬라이싱 [시작경계: 끝경계: 간격]
    print("[::2] 슬라이싱:", str1[::2]) #전체에서 2 간격으로 슬라이싱 ->Pto
    print ("[::-1] 슬라이싱:",str1[::-1]) #간격값이 음수일 때: 역순으로 복제


    #연결 (+) -> 산술 연산이 아님
    print(str1 + " Programing")

    #반복 (*)
    print(str1*3) #str1을 3번 반복

    #포함여부 (in/not in) -> boolean 값으로 반환: True or False
    print("P" in str1)
    print("P" not in str1)

def transform_methods():
    """
    대소문자 변환 관련 메서드들
    """
    s= "i like Python"
    print("원본:" +s)
    print("UPPER:" + s.upper()) # 모두 대문자로
    print("lower:" +s.lower()) #모두 소문자로
    print("SWAPCASE:"+s.swapcase()) #대문자<->소문자
    print ("Capitalize:"+ s.capitalize()) #문장의 첫글자를 대문자로
    print("Title:"+s.title()) #기사 제목 형태로: 각 단어의 첫글자를 대문자로 변환

    print("원본:" +s) # 원본은 변경되지는 않는다; 새로운 객체가 생성될뿐!


def search_methods():
    """
    문자열 검색 관련 메서드 연습
    """

    s= "I Like Python, I Like Java Also"
    print("원본:", s)
    print("COUNT:", s.count("Like")) # Like의 갯수
    print("1st Find:", s.find("Like")) #문자열 내의 Like 인덱스
    print("2nd Find:", s.find("Like",6)) #6번 인덱스 이후의 Like 인덱스
    print("3rd Find:", s.find("Like",20)) #없는 검색 결과는 -1로 반환함

    print("1st index:", s.index("Like")) #문자열 내의 Like 인덱스
    print("2nd index:", s.index("Like",6)) #6번 인덱스 이후의 Like 인덱스
    #print("3rd index:", s.index("Like",21)) #substring not found --> ValueError (!): 없는 검색 결과는 ERROR
    #에러 발생시키는 메서드 사용시에는 미리 체크 (방어 코딩)

    if "Like" in s[21:]:print ("3rd Index", s.index("Like",21))

    #역방향 검색: rfind, rindex
    print("RFIND:", s.rfind("Like"))
    print("2nd RFIND:", s.rfind("Like",0,17)) #0~17경계 사이에서 Like 역방향 검색
    #rindex는 검색 결과가 없을때 ValueError발생; 그 외에는 rfind사용방법과 동일
    print("RINDEX:",s.rindex("Like"))
    print("2nd RINDEX:",s.rindex("Like",0,17))

    #Index 메서드를 사용할때에는 미리 in 메서드로 확인을 하고 사용하자(!)

    #특정 문자열로 시작 or 끝나는가?
    url= "http://www.naver.com"
    surl="https://www.naver.com"
    ftp= "ftp://ftp.naver.com"
    print ("url이 http://로 시작?", url.startswith("http://"))
    print ("surl이 http://로 시작?", surl.startswith("https://"))

    #검색시, 시작 문자열을 여러개 중 한개로 비교할 때 --> tuple()로 묶어주기
    print("ftp가 http:// or https://로 시작?", ftp.startswith(("http://", "https://")))
    print("url이 http:// or https://로 시작?", url.startswith(("http://", "https://")))

    #endswith
    print ("url이 naver.com으로 끝나는가?", url.endswith("naver.com"))

    #startswith, endswith: 범위 지정하기
    print("ftp의 6~20까지의 범위 중에서 ftp.으로 시작?", ftp.startswith("ftp.",6,20))

def modify_replace_methods():
    """
    문자열 수정, 치환 관련 메서드들
    """
    s= "                  Alice and the Heart Queen          "
    print("STRIP:[", s.strip(), "]", sep="") #앞뒤의 공백문자 제거
    print("LSTRIP:[", s.lstrip(),"]", sep="") #왼쪽 (앞)의 공백문자 제거
    print("RSTRIP:[", s.rstrip(), "]", sep="") #오른쪽 (뒤)의 공백문자 제거

    #기본적으로 strip은 공백문자를 제거 -> 임의의 문자열의 제거도 가능
    s="------------Alice and the Heart Queen------------"
    print("Strip -:[",s.strip("-"),"]", sep="") #앞뒤의 "-" 문자를 모두 제거

    s="I love Java"
    print("원본:", s)
    print("REPLACE:",s.replace("Java", "Python")) #Java를 Python으로 변경


def split_join_method():
    """
    분할과 합치기 메서드
    """
    s="Ham and Cheese and Breads and Ketchup"
    print("원본:",s)
    print("SPLIT:", s.split()) #기본값: 공백문자를 기준으로 분리
    items=s.split(" and ") #분할 시, " and "를 기준으로 분리
    print("SPLIT:", items)

    items=s.split(" and ", 2) # " and " 구분자를 기준으로 앞으로만 2개만 추출
    print("SPLIT:",items) # [Ham, Cheese, Breads and Ketchup]으로 결과가 나옴
    items= s.rsplit(" and ", 2) # " and " 구분자를 기준으로 뒤로부터 2개만 추출
    print("SPLIT:", items)

    lines = """
Java Programming
Python Programming
Oracle Database
    """
    print(lines.split()) #공백문자를 기준으로 (공백문자: 스페이스, 개행, 탭) 분할
    print(lines.splitlines()) #개행문자 기준으로 분할
    print(lines.splitlines(True)) #개행문자를 삭제하지 않고 유지

def check_methods():
    """
    판별 관련, 주로 is 계열 메서드 --> boolean값으로 반환
    """
    print("1234567890".isdigit()) #문자열이 숫자만 포함?
    print("abcdefg".isalpha()) #문자열이 알파벳만 포함?
    print("Python3".isalnum()) #문자열이 알파벳과 숫자만 포함? -둘중 하나가 없어도 True
    print("Python 3".isalnum()) #공백문자 포함-> alnum이 아님
    print("\r\n\t".isspace()) #공백문자만 포함?
    print("".isspace()) #공백문자가 아님으로 판명

    print("PYTHON".isupper()) #전부 대문자?
    print("python".islower()) #전부 소문자?
    print("Python Programming".istitle()) #문자열이 title형태?

def align_methods():
    """
    문자열 정렬 메서드
    """
    s="Alice and the Heart Queen"
    print("CENTER:[",s.center(60),"]", sep="") #60자리 확보 중앙 정렬
    print("CENTER:[",s.center(60,"*"),"]", sep="") #빈자리를 *로 채우기
    print("LJUST:[",s.ljust(60,"*"),"]",sep="") #왼쪽 정렬
    print("RJUST:[", s.rjust(60,"*"),"]", sep="") #오른쪽 정렬

    print("ZFILL:", "1234".zfill(5)) #5자리 확보+ 빈자리는 0으로 채움 result:01234
    print("ZFILL:", "1234567890".zfill(5)) #확보한 자릿수는 최소 공간 -> 자릿수가 넘어가도 내용은 잘리지 않음


def string_format():
    """
    문자열 포맷 정리
    """
    #C Style 문자열 포맷
    #%s (문자열). %c, %d(정수), %f(실수), %o, %x, %%(Literal %)

    fmt = "%d개의 %s 중에서 %d개를 먹었다."
    print (fmt %(10,'사과',3))
    print("현재 이자율은 %.2f%%입니다." %1.2345) #%f 포맷은 부가적으로 소숫점 자리를 제한할 수 있다.

    #named formatting (parameter 방식)
    #바인딩 순서에 유의하지 않아도 됨
    fmt="%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다."
    print (fmt%{"total":10, "eat":3, "fruit": "사과"})

    #format 메서드
    fmt = "{}개의 {} 중에서 {}개를 먹었다."
    print(fmt.format(10,"사과",3))
    fmt= "{0}개의 {1} 중에서 {2}개를 먹었다." #parameter의 순서 명시
    print(fmt.format(10,"사과", 3))
    fmt="{total}개의 {fruit} 중에서 {eat}개를 먹었다."
    print(fmt.format(eat=3, fruit="사과", total=10)) #함수의 인자 형태로 전달

    # 사전 객체 이용한 named parameter 연결: .format_map
    data= {
        "total":10, "fruit":"사과", "eat":3
    }
    print(fmt.format_map(data))

    #가장 최신 스타일: F-문자열 (ab ver 3.6)
    #문자열 앞에 f or F
    #변수의 이름 or 표현식 {} 안에 포함해서 값을 문자열로 가져온다.
    total, fruit, eat = 10, 'apple', 3
    print(f"{total}개의 {fruit.upper()} 중에서 {eat}개를 먹어서 {total-eat}개가 남았다.")

if __name__ == "__main__":
#    define_str()
#    string_oper()
#    transform_methods()
#    search_methods()
#    modify_replace_methods()
#    split_join_method()
#    check_methods()
#    align_methods()
    string_format()
