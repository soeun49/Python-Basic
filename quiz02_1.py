def question1():
    x=int(input("score1:"))
    y=int(input("score2:"))

    average = (x+y)/2
    if x >=50:
        print()
    if y>=50:
        print()
    if average >=60:
        print("합격!")
    else:
        print("불합격")

if __name__ == "__main__":
    question1()