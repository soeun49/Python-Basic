def question3():

    sum=0

    while True:
        s=str(input('methods:'))
        if s=="d":
            d=int(input('Amount:'))
            sum+=d
            print('Balance:',sum)
            continue
        if s=="w":
            w=int(input('Amount:'))
            sum-=w
            print('Balance:',sum)
            continue
        if s=="f":
            break
        else:
            print("?")
            break



if __name__ == '__main__':
    question3()