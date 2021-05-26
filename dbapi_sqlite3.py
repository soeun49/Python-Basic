#모듈 임포트
import sqlite3,os
from sqlite3 import Error

#접속 함수
def create_connection(db_file):
    #./database 디렉터리 생성
    if not os.path.exists("./database"): #현재 디렉터리 아래 database 디렉터리가 없으면
        os.makedirs("./database") #생성하기

    #접속
    try:
        conn = sqlite3.connect(db_file) #db_file로 데이터베이스의 접속; 성공시 Connection 객체 반환
        print(sqlite3.version)
    except Error as e:
        print (e,type(e))
        return None #접속 실패 시, None
    return conn


def test_connection(db_file):
    conn = create_connection(db_file)
    print(type(conn))
    conn.close()

def test_create_table(db_file):
    #접속
    conn = create_connection(db_file) # Connection 객체 반환

    #커서 획득
    cursor= conn.cursor() # Cursor 객체 반환

    #sql 작성
    ddl= """CREATE TABLE IF NOT EXISTS 
    customer 
        (id integer primary key autoincrement,
         name varchar(20),
         category integer,
         region varchar(10))    
    """
    #sql 실행
    cursor.execute(ddl)

    #접속 해제
    conn.close()


#파라미터 이용 insert
def test_insert_data(db_file,name,category, region):
    conn=create_connection(db_file)
    cursor=conn.cursor()

    # 익명 parameter 바인딩
    sql ="""INSERT INTO customer (name, category, region) VALUES(?,?,?)"""
    res= conn.execute(sql,(name, category, region))

    #INSERT, UPDATE, DELETE -> 영향 받은 레코드의 수가 .rowcount로 반환
    print("{}개의 레코드가 영향을 받음.".format(res.rowcount))
    conn.commit()
    conn.close()

def test_delete_all(db_file):
    conn = create_connection(db_file)
    sql= "DELETE FROM customer"
    res= conn.execute(sql)

    print("{}개의 레코드가 삭제됨.".format(res.rowcount))
    conn.commit()
    conn.close()

def test_insert_bulk_data(db_file):
    #테스트 데이터 여러개 insert
    test_delete_all(db_file) #비우고
    test_insert_data(db_file, "둘리", 1, "부천")
    test_insert_data(db_file, "고길동",2,"부천")
    test_insert_data(db_file, "김소은",2,"서울")
    test_insert_data(db_file,"홍길동", 1, "서울")
    test_insert_data(db_file,"이수민",2,"부산")

def test_select_data(db_file):
    # conn=create_connection(db_file)
    with create_connection(db_file) as conn:
        # select 쿼리 수행
        sql= "SELECT * FROM customer"
        cursor=conn.execute(sql)

        print(type(cursor))
        # 결과 처리
        print(cursor.fetchone()) #1개 레코드 불러오기
        print(cursor.fetchmany(2)) #2개 레코드 불러오기
        print(cursor.fetchall()) #현재 커서 위치에서 나머지 레코드 불러오기

    # conn.close()

def test_search_data(db_file):
    conn=create_connection(db_file)

    #명명된 placeholder
    #   placeholder에 :key로 명명
    #   데이터는 dict로 전달
    sql="""\
    SELECT name, category, region FROM customer WHERE region=:region or category=:category
    """
    cursor=conn.execute(sql,{"region": "부천", "category": 2})

    for customer in cursor.fetchall(): #전체 데이터를 루프로 돌림
        print(customer)


if __name__ == "__main__":
    db_file= "./database/mysqlite.db"
    # test_connection(db_file)
    # test_create_table(db_file)
    # test_insert_data(db_file,'둘리',2,'부천')
    # test_insert_bulk_data(db_file)
    # test_select_data(db_file)
    test_search_data(db_file)


