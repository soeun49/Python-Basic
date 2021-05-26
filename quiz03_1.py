def question1():

    while True:
        x = input("수를 입력하세요")
        a= x.isdigit()

        if a is not True:
            print("정수가 아닙니다. 다시입력하세요")
            continue

        if a is True:
            to=int(x)
            total = 0
            for i in range(0, to+1,3):
                # if i%3 == 0:
                    total +=i

                    print("1부터 {}까지의 3의 배수의 합 = {}".format(to, total))
        break


if __name__ == '__main__':
    question1()
