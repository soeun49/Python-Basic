def question1():
    x=int(input("Score1:"))
    y=int(input("Score2:"))
    average= (x+y)/2

    if x>=50:
        print()
    if y>=50:
        print()
    if average>=60:
        print("합격!")
    else:
        print("불합격")

if __name__=="__main__":
    question1()