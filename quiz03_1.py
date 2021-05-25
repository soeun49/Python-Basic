def question1():

    while True:
        x = input("수를 입력하세요")
        total = 0
        a= x.isdigit()
        if a is not True:
            print("정수가 아닙니다. 다시입력하세요")
            continue

        if a is True:
            x=int(x)
            for x in range (0,x+1,3):
                total+=x
                print("1부터", x+1, "까지 3의 배수의 합=",total,end="")
                print()
        else:
            print()
            break

    else:
        print()


if __name__ == '__main__':
    question1()
