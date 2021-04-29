# Chpater06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해,,
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능

# 인스턴스 변수 : 객체마다 별도 존재
# 예제1

class Dog(object):
    # 클래스 속성
    specices = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)
print()

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2)

# 비교
print(a == b, id(a), id(b), id(c))
print()

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)
print()

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))
print()

if a.specices == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.specices))
print()

print(Dog.specices)
print(a.specices)
print(b.specices)
print()

# 예제2
# self의 이해
class selfTest:
    def func1():        # self가 없는것은 클래스 메소드
        print('Func1 called')
    def func2(self):    # self가 붙은것은 인스턴스 메소드
        print('Func2 called')

f = selfTest()

print(dir(f))
print()

print(id(f))

#f.func1() # 예외(에러남)
f.func2()
#selfTest.func2()   # 예외(에러남)
selfTest.func1()
selfTest.func2(f)
print()

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0   # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print(user1.stock_num)

del user1
print('after', Warehouse.__dict__)
print()

# 예제4
class Dog1(object):
    specices = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# 인스턴스 생성
c = Dog1('july', 4)
d = Dog1('marry', 10)
# 메소드 호출
print(c.info())
print(c.speak('wal wal'))
print(d.info())
print(d.speak('wal wal'))
