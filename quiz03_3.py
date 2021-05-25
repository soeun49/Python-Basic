args=int(input("입력:").split(" "))

def sum(*args):
    total=0
    for x in args:
        total+=x
    return total

def max(*args):
    for x in args:
        return max(x)

def min(*args):
    for x in args:
        return min(x)

def avg(*args):
    total=0
    for x in args:
        total+=x
        avg=total/len(x)
        return avg

print()
# print(total,maxval,minval,avg)