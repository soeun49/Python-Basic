def question2():
    for x in range(1,10):
        print("구구단", x, "단", sep="")
        for i in range(1,10):
            print(x, "x", i, "=", x * i)
        print("---------------------")


if __name__=='__main__':
    question2()

