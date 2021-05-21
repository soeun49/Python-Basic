def question3():
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

    print(students,type(students))
    print(students[:1],type(students[:1]))
    print(students[1:],type(students[1:]))

    lee=students.pop()
    kim=students.pop()
    print(lee)
    print(kim)

    lst=list(kim.values())
    print(lst)
    lst=lst[1:]
    print(lst)
    total=sum(lst)
    average=sum(lst)/len(lst)
    print("합계", total)
    print("평균", average)
    kim['total']=total
    kim['average']=average

    lst2=list(lee.values())
    print(lst2)
    lst2=(lst2[1:])
    print(lst2)
    total=sum(lst2)
    average=sum(lst2)/len(lst2)
    print("합계", total)
    print("평균", average)

    lee ['total'] = total
    lee ['average']=average

    print(kim)
    print(lee)

    students=[]
    students.append(kim)
    students.append(lee)
    print(students)

    # kor=(lst[1:2]+lst2[1:2])
    # eng= (lst[2:3] +lst2[2:3])
    # math = (lst[3:] + lst2[3:])






if __name__=="__main__":
    question3()