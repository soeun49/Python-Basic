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


def test_lifecycle():
    p1=Point(10,20) #생성자 사용
    print("instance count:", Point.instance_count)

    p2=Point() #기본값 사용
    print("instance count:",Point.instance_count)

    print(p1,p2)

def test_print():
    p1=Point(10,10)
    print("p1:",p1) #__str__호출

    #__str__은 일반 사용자가 보기 쉽게 출력하는 포맷
    #__repr__은 개발자가 객체를 복원하기 위해 출력하는 포맷

    print(repr(p1)) #__repr__호출
    p2=eval(repr(p1))
    print("p2:",p2,type(p2))


    #__str__비공식적 문자열 (일반 사용자용)
    #__repr__공식적 문자열 (개발자용)


def arith_oper_overriding():
    p1=Point(10,20)
    p2=Point(30,40)

    # print(dir(object))
    # Point + Point
    print(p1+p2)
    #TypeError: unsupported operand

    #Point + int
    p1=Point(10,20)
    print (p1+10)

    #int + Point
    p1=Point(10,20)
    print("int+point:",10+p1)

    #연습문제
    p1=Point(10,20)
    p2=Point(30,40)
    print(p1-p2)

    p1=Point(10,20)
    print(p1-10)

    p1= Point(10,20)
    p2= Point(10,20)

    print("p1==p2?", p1==p2) #false로 나옴


if __name__=="__main__":
    # bound_class_method()
    # unbound_class_method()
    # class_member_test()
    # test_lifecycle()
    # test_print()
    arith_oper_overriding()