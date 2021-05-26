import sqlite3

class Database:
    #생성자
    def __init__(self,db = None): #none은 기본값
        self.conn=None
        self.cursor=None

        if db: #db parameter가 전달되었으면
            self.open(db)

    #접속 함수
    def open(self,db):
        try:
            self.conn=sqlite3.connect(db)
            self.cursor=self.conn.cursor()
        except sqlite3.Error as e:
            print("Database 접속 실패")

    #닫기 메서드
    def close(self):
        if self.conn:
            self.conn.commit() #남아있는 I,U,D(Insert, Update, Delete)쿼리를 커밋
            self.cursor.close()
            self.conn.close()

    #__enter__: with와 함꼐 사용했을 때 호출되는 생명주기
    def __enter__(self):
        return self


    #__exit__: with절이 끝났을때 호출되는 생명주기
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.close()


    #SELECT 쿼리 수행 메서드
    def execute_select(self,sql,parameter=None):
        if parameter is not None: #parameter가 존재하면
            self.cursor.execute(sql,parameter)
        else: #parameter가 없으면
            self.cursor.execute(sql)

        data=list(self.cursor.fetchall())
        return data

    #Insert, Update, Delete 쿼리 수행 메서드
    def execute_cud(self,sql,parameter=None):
        if parameter is not None:
            self.cursor.execute(sql,parameter)
        else:
            self.cursor.execute(sql)

        #영향받은 레코드 개수 반환
        return self.cursor.rowcount


