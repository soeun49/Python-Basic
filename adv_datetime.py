#datetime module
    #datetime class, date class, time class

import datetime #datetime module import
def get_datetime():
    #시간의 획득: 현재 날짜와 시간
    now = datetime.datetime.now()
    print(now)

    #생성자를 이용하여 날짜를 지정할 수 있음
    dt=datetime.datetime(1999,12,31) #최소 년,월,일을 지정해줘야 함
    print(dt)

    #datetime의 주요 속성들
    print("date관련 속성:",dt.year,dt.month, dt.day)
    print("time관련 속성:", dt.hour,dt.minute,dt.second,dt.microsecond)

    #요일 확인: weekday-> 월요일:0~일요일:6
    print("오늘은 무슨요일?", now.weekday())

    #datetime객체는 date 객체 + time 객체
    print(now.date(),type(now.date())) #날짜 관련 속성을 가진 date 객체
    print(now.time(), type(now.time())) #시간 관련 속성을 가진 time 객체

    #date 객체는 datetime클래스의 날짜 관련 속성과 요일 메서드 이용
    #time객체는 datetime클래스의 시간 관련 속성을 이용
    nowdate=datetime.datetime.now().date()
    nowtime=datetime.datetime.now().time()
    print("date:", nowdate.year,nowdate.month,nowdate.day,nowdate.weekday())
    print("time:",nowtime.hour,nowtime.minute,nowtime.second,nowtime.microsecond)

def timedelta_ex():
    """
    timedelta: 두 datetime사이의 간격 정보 객체
    """
    current=datetime.datetime.now()
    print("CURRENT:",current)
    past=datetime.datetime(1999,12,31)
    print("PAST:",past)

    #두 datetime의 대소 비교
    print("CURRENT가 PAST보다 이후인가?", current>past)

    #datetime-datetime=timedelta

    diff= current-past
    print(diff,type(diff))

    #timedelta의 속성
    print("timedelta:", diff.days, diff.seconds,diff.microseconds)
    print("total seconds:", diff.total_seconds()) #모든 속성을 초 단위로 모아서 변환

    #datetime+timedelta= new datetime
    #현재 시간에서 100일후 정보
    print("current:", current)
    diff=datetime.timedelta(100,0,0)
    print("100일 후:",current+diff)

def format_date():
    """
    문자열의 포맷
        datetime -> str: strftime()
        str -> datetime: strptime()
    """
    current=datetime.datetime.now()
    print("current",current)

    #datetime -> str: strftime()
    print(current.strftime("%Y-%m-%d %H:%M"))
    print(current.strftime("%Y년 %m월 %d일 %H시 %M분"))

    #str -> datetime: strptime()
    s="2021-05-24 17:00:00" #실제 데이터와 문자열이 일치해야 함
    dt=datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    print(dt,type(dt))

if __name__ == "__main__" :
    # get_datetime()
    # timedelta_ex()
    format_date()