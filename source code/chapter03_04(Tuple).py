# Chpater03-4
# 파이썬 튜플
# 리스트와 비교 중요!
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # = 불변

# 선언
a = ()      # 튜플 선언은 ()가 있어야 한다.
b = (1,)    # 뭔가 들어가면 쉼퓨, 를 써줘야 한다.
c = (11,12,13,14)
d = (100,1000,'Ace', 'Base', 'Captine')
e = (100,1000,('Ace', 'Base', 'Captine'))

# 인덱싱
print('--------indexing--------')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))   # tuple을 list로 형변환 가능, 단 불변의 성질은 사라진다.
print()

# 수정x
# d[0] = 1500 x

# 슬라이싱
print('-------slicing-------')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])
print()

# 튜플 함수
a = (5,2,3,1,4)
print('--------function of tuple-------')
print('a - ', a)
print('a - ', a.index(4))        # index는 해당 값을 가진 index를 가져온다.
print('a - ', a.count(2))
print()

# 패킹 & 언패킹

# 패킹 (패킹은 그냥 선언 자체가 패킹이야. 묶는거니까)
print('--------packing-------')
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])
print()

# 언패킹
(x1, x2, x3, x4) = t    # 괄호가 없어서 상관은 없음,, 가독성있게 () 쳐주는게 좋긴함

print(type(x1), type(x2), type(x3), type(x4))   # 출력해보면 str으로 바뀜
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1,2,4  # 괄호가 없어도 튜플임
t3 = 4,     # 이건 튜플 선언임
x1, x2, x3 = t2     # 이건 언팩킹임
x4, x5, x6 = 4,5,6  # 이것도 언팩킹임

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)
