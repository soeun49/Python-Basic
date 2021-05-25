def question2():
    lst = [1, 3.14, 'python', 7, 89.1, 3]

    lst_cleaned=[]

    for item in lst:
        if isinstance(item,(int,float)):
            lst_cleaned.append(item)

            print("Cleaned List",lst_cleaned)
    else:
        print()









if __name__ == '__main__':
    question2()
