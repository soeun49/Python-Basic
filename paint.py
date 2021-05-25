# Test
from point import Point

def bound_class_method():
    #직접 인스턴스 명시 -> 멤버에 접근
    p=Point() #생성
    p.setX(10)
    p.setY(20)
    print(p.getX(),p.getY(),sep=",")
    print(p.getX, p.getY)

    #getX, getY가 bound method로 실행

def unbound_class_method():
    #클래스에 인스턴스를 전달해서 인스턴스 내부의 메서드 호출
    p=Point()
    Point.setX(p,10)
    Point.setY(p,20)
    print(Point.getX(p),Point.getY(p))
    print(Point.getX,Point.getY)

    #getX, getY가 클래스 내부의 함수로 실행됨

def class_member_test():
    p1=Point()
    p1.setX(10)
    p1.setY(20)

    print("p1: {},{}".format(p1.getX(),p1.getY()))
    print("instance_count:",
          p1.instance_count, #인스턴스에서 접근 가능
          Point.instance_count) #인스턴스 없이도 접근 가능

if __name__=="__main__":
    # bound_class_method()
    # unbound_class_method()
    class_member_test()