def question1():

    s= "Life is too short, You need Python"

    print(s.lower())
    print(s.lower().replace(" ","").replace(",",""))
    lst=list(s.lower().replace(" ","").replace(",",""))
    print(lst)
    chars=set(lst)
    print(chars)
    lst2=list(chars)
    print(lst2,type(lst2))
    lst2=sorted(lst2)
    print(lst2)




if __name__ == '__main__':
    question1()

