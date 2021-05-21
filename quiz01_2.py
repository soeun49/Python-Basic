def question2():
    lst=[1,2,3,4,5,6,7,8,9,10]

    slice=lst[3:7]
    print (slice)
    sort= sorted (slice, reverse=True)
    print(sort)
    print(lst)

    lst[3:7]=sort
    print(lst)


if __name__ == "__main__":
    question2()
