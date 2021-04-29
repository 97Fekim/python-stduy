# Chpater08-1
# 파이썬 내장(built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 실습

# 절대값
# abs()
print(abs(-3))
print()

# all : iterable 요소 검사(참,거짓)
print(all([1,2,3])) # 모두 true일 때만 true를 리턴(and)
print(any([1,2,0])) # 하나만 true여도 true를 리턴(or)
print()

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(67))
print(ord('c'))

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter 함수 : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1,-3,2,0,-5,6])))
print(list(filter(lambda x : abs(x) > 2, [1,-3,2,0,-5,6])))
print()

# id : 객체의 주솟값(레퍼런스) 반환
print(id(int(5)))
print()

# len : 요쇼의 길이 반환
print(len('abcdefg') - 1)
print(len([1,2,3,4,5,6,7]))
print()

# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('pythonstudy'))
print()

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,-6])))
print(list(map(lambda x : abs(x), [1,-3,2,0,-5,-6])))
print()

# pow : 제곱값 변환
print(pow(2,10))
print()

# range : 반복가능한 객체(Iterable) 변환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))
print()

# round : 반올림
print(round(6.5781, 2))
print(round(5.6))
print()

# sorted : 반복가능한 객체(Iterable)를 정렬 후 반환
print(sorted([6,7,4,3,1,2]))
a = sorted([1,9,4,5,3,1,7,46])
print(a)
print(sorted(['p','y','t','h','o','n']))
print()

# sum : 반복가능한 객체(Iterable)
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))
print()

# type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))
print()

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30], [40,50,70])))
print(list(zip([10,20,30], [40,50])))
