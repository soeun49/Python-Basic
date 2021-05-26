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
        except:sqlite3.Error as e:
            print("Database 접속 실패")

    #닫기 메서드
    def close(self):
        if self.conn:
            self.conn.commit() #남아있는 I,U,D(Insert, Update, Delete)쿼리를 커밋
            self.cursor.close()
            self.conn.close()



