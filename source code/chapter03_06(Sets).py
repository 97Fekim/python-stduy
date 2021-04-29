# Chpater03-6
# 집합(Set) 특징
# 집합(Set) 자료형은 (순서x, 중복x, 추가o, 삭제o)

# 선언
a = set()
b = set([1,2,3,4])  # set를 초기화 할 때는 list형태로 넣어준다.
c = set([1,4,5,6])
d = set([1,2,'Pen', 'Cap', 'Plate'])    # 서로 다른 자료형도 섞을 수 있다.
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # {} 를 썼다고 모두 dict가 아니다. key없이 선언 되었다면 set이다.
f = {42, 'foo', (1,2,3), 3.141592}

print('a - ', type(a), a, 2 in a)
print('b - ', type(b), b, 4 in b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)


# 튜플 변환(set -> tuple)
t = tuple(b)    # 튜플로 변환 되었다 -> 슬라이싱[1:3] 등의 성질 이용 가능하다.
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
print()

# 리스트 변환
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(e, len(e))    # e에 'foo'가 2개가 있어서 하나는 없어짐,, 중복이 안되기 때문에
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))    # .intersection()는 교집합을 구하는데 쓰인다.

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union((s2)))     # .union() 함수는 합집합을 구하는데 쓰인다.

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))  # .difference() 함수는 차집합을 구하는데 쓰인다.
print()

# 중복 원소 확인
print('s1 & s2 ? : ', s1.isdisjoint(s2))    # .isdisjoint() 함수는 교집합이 없는지 체크하는 함수이다.
print()

# 부분 집합 확인
print('is subset?' , s1.issubset(s2))      # .issubset()은 s1이 s2의 부분집합이냐?? 를 체크하는 함수이다.
print('is superset?' , s1.issuperset(s2))    #

# 추가 & 제거
s1 = set([1,2,3,4])
s1. add(5)           # set에는 추가가 직관적이다. (.add())
print('s1 - ', s1)
s1.remove(1)         # .remove()로 간단히 지울수 있다
print('s1 - ', s1)
s1.discard(4)       # .discard()로도 간단히 지울수 있다. 근데 discard는 없는걸 지워도 에러가 나지 않는다.
print('s1 - ', s1)  # .discard()는 예외가 발생하지 않는다.(메소드 내부적으로 예외처리가 다 되어있다.)
s1.clear()          # .clear()로 싹 비우는게 가능하다.
print('s1 - ', s1)
