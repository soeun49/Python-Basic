def q1():
    #몇 개의 알파벳 글자가 사용되었는지 판별
    s= "Life is too short, You need Python"

    s= s.lower()\
        .replace(",","")\
        .replace(" ","")

    lst=list(s)

    chars=set(lst)
    print("chars:",chars)

    #다시 리스트로
    lst=list(chars)
    lst.sort() #알파벳 순으로 저열ㄹ
    print(lst)
    print(len(lst),"개의 알파벳이 사용되었습니다")

def q2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice= lst[3:7]
    slice.reverse() #순서 반전
    lst[3:7]=slice
    print(lst)
    print(lst==[1,2,3,7,6,5,4,8,9,10])

def q3():
    students = [
        {
            "name": "Kim",
            "kor":80,
            "eng":90,
            "math":80
        },
        {
            "name":"Lee",
            "kor":90,
            "eng":85,
            "math":85
        }
    ]

    for student in students:
        total= student.get("kor")+student.get("eng")+student.get("math")
        average=total/3

        student['total']=total
        student['average']=average

    print(students)

if __name__ =="__main__":
    # q1()
    # q2()
    q3()