# Chpter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용!!
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# [리스트]
# (튜플)
# {딕셔너리}

# 왼쪽 = key, 오른쪽 = value
# 선언
a = {'name' : 'Kim', 'phone' : '01090374099', 'birth' : '870514'}
b = {0: 'Hello Python'}
c = {'arr' : [1,2,3,4]}

d = {
    "Name" : 'Nice man',
    'City' : 'Seoul',
    'Age'  : 33,
    'Grade': 'A',
    'Status':True
}

e = dict([
    ('Nmae' , 'Nice man'),
    ('City' , 'Seoul'),
    ('Age'  , 33),
    ('Grade', 'A'),
    ('Status',True)
])

f = dict(   # 이 방법을 주로 이용한다.
    Name = 'Nice man',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(a), e)
print('f - ', type(e), f)

# 출력
print('a - ', a['name'])        # a[]로 접근하면 index가 없을 때 에러가 난다.
print('a - ', a.get('name1'))   # get으로 접근해야 확실하다.
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f['Name'])
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)

# 딕셔너리 길이
a['name'] = 'Park'  # 이러면 name이 수정이 된다.
print('a - ', a)
print('a - ', len(a))   # dict의 len을 호출하면 key의 갯수가 호출된다.
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_key, dict_values, dict_items : 반복문(__iter__)에서 사용 가능,,

print('a - ', a.keys()) # .keys() 함수는 key값들만 호출한다.
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', list(d.keys()))   # 이렇게 리스트로 형변환 할 수도 있다.
print()

print('a - ', a.values())   # .values() 함수는 valus값들만 호출한다
print('b - ', b.values())
print()

print('a - ', a.items())    # .items() 함수는 key와 value를 모두 tuple 형태로 호출한다.
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))  # 이렇게 리스트로 변환해서 사용하면 좋다.
print()

print('a - ', a.pop('name'))    # pop을 하면 dict에서도 꺼내고 제거가 된다.
print('a - ', a)
print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())  # .popitem()으로 dict의 아이템들을 제거할 수 있다.
print('f - ', f)            # 추첨기 같은거 만들때 사용하는거라고 생각하면 될 듯.
print('f - ', f.popitem())
print('f - ', f)
print()

print('a - ', 'birth' in a) # birth라는 key가 a dict 안에 있어?
print('d - ', 'City' in d)  # City라는 key가 d dict 안에 있어?
print()

# 메소드를 이용한 딕셔너리수정
a.update(birth = '910904')  # .update() 메소드로 수정이 가능하다. 주의할 것은 key값 parameter에 ''는 없어야 한다
print('a - ', a)
print()
temp = {'address' : 'Busan'}    # 이렇게 temp에 보관한 다음에 update를 쓸 수 도 있다.
a.update(temp)
