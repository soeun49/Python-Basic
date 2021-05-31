print(6/2 not in (2,4,6))

data="Python"
print(len(data))

t=(1,2,3,4)
print(t[1:4])

d = {"baseball":9, "soccer": 11}
# d['volleyball']=6
# d[[1,2,3]]=12
print(d)

p="total %d, mine %d".format(10,3)
print(p)

p="python"*3
print(p)
lst=[1,2,3,4]
for index,color in enumerate(lst):
    print(index,color)

lst=[1,2,3,4]
lst2=[5,6,7]
lst.extend(lst2)
print(lst)

def calc(a,b,func):
    if (callable(func)):
        return func(a,b)
print(calc(3,4,lambda x,y: x*y))

def get_last_item(x):
    if isinstance(x,(tuple,list)):
        return x[-1]
    else:
        return None

print(get_last_item((1,2,3)))