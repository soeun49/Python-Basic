#오라클에 접속
#terminal: pip install cx_Oracle -> install 하기

import cx_Oracle #모듈 임포트

def create_connection():
    #dsn (data source name 작성 필요)
    dsn=cx_Oracle.makedsn("localhost",1521,"xe") #서버주소, 포트, SID (서비스명)

    #접속
    db= cx_Oracle.connect("hr","hr",dsn) #계정, 암호, 데이터 소스이름
    return db


def test_connect():
    #접속
    conn=create_connection()
    print(type(conn))
    conn.close()

def test_basic_query():
    #hr.employees 모든 레코드 반환
    conn=create_connection() #Connection
    cursor=conn.cursor() #Cursor

    #SQL 실행
    sql="SELECT * FROM employees"
    cursor.execute(sql)

    # print(cursor)
    print("fetchone")
    print(cursor.fetchone())
    print("fetchmany")
    print(cursor.fetchmany())

    for row in cursor.fetchall():
        print(row)

    conn.close()

def test_placeholder():
    conn=create_connection()
    cursor=conn.cursor()
    sql="SELECT * FROM employees WHERE last_name=:1 or last_name=:2"
    cursor.execute(sql,("King","Grant")) #튜플 형식으로 불러옴 not in form of dict

    for record in cursor:
        print(record)

    conn.close()

def test_dictionary():
    conn=create_connection()
    cursor=conn.cursor()

    #SQL 실행
    sql="SELECT * FROM employees"
    cursor.execute(sql)

    # print(dir(cursor))
    print(cursor.description) #커서의 정보 확인

    #실제 컬럼 정보와 레코드를 쌍으로 묶어서 zip -> 사전화
    for record in cursor:
        #사전 생성
        record_dct=dict(zip([d[0]for d in cursor.description],record))
        print(record_dct) # 컬럼명과 정보를 보기 쉽게 사전 형태로 만들어 냄


    conn.close()
if __name__=="__main__":
    # test_connect()
    # test_basic_query()
    # test_placeholder()
    test_dictionary()
