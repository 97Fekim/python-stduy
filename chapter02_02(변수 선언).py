# Chapater02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 100.0
print(n)
print(type(n))
print()

# 동시
x = y = z = 700
print(x,y,z)
print()

# 재선언
var = 75
print(var)
print(type(var))
print()

var = 'change value'
print(var)
print(type(var))
print()

n = 777
print(n, type(n))
m = n
print(m, type(m))
m = 400
print(m, type(m))

# id(identity) // 객채의 고유값 확인
m = 800
n = 600
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 아래의 경우에는 같은 오브젝트를 참조한다.
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# camel case : numberOfCollegeGraduates (대,소문자 혼용) -> method 선언에 주로 씀
# Pascal Case : NumberOfCollegeGraduates (위와 동일, 앞글자만 대문자) -> class 선언에 주로 씀
# Snake Case : number_of_college_graduates (언더바 사용)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 7

#  예약어는 변수명으로 불가능
"""
False def if raise
None del import return
True elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not
class from or
continue global pass
"""
