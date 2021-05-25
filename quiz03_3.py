def summary(*args):
    total=sum(args)
    return total, max(args), min(args), total/len(args)

def q3():
    total,maxval,minval,avg=summary(80,75,90,95,85)
    print(total,maxval,minval,avg)

if __name__ == "__main__":
    q3()
