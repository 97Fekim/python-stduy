# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요!!!!
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70,75,80,85]
d = [1000,10000,'Ace','Base','Cpatine']         # 서로 다른 자료형도 같이 담을 수 있다.
e = [1000, 10000, ['Ace', 'Base', 'Captine']]   # 다른 리스트도 끼워 넣기가 가능하다.
f = [21.42, 'Foobar', 3, 4, False, 3.141592]

# 인덱싱
print("-------indexing------")
print('d - ', type(d), d)
print('d[1] - ', d[1])         # 인덱스를 가져오는 법
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])            # -1 인덱스는 끝놈
print('e - ', e[-1][1])         # 리스트속 리스트는 다음과 같이 호출.
print('e - ', list(e[-1][1]))   # 리스트로 형변환하면 알아서 쪼개준다.
print()

# 슬라이싱
print('-------slicing------')
print('d - ', d[0:3])           # d에서 0부터 3까지 나와라
print('d - ', d[2:])            # d 2부터 끝까지 나와라
print('e - ', e[-1][1:3])       # e속 -1번째 리스트에서 1인덱스부터 3까지 나와라
print()

# 리스트 연산
print('----calculation of lis----')
print('c + d = ', c+d)          # 리스트를 더하면, 앞 리스트에 뒷 리스트가 뒤에 삽입된다.
print('c * 3 = ', c * 3)        # 리스트에 상수를 곱하면, 값이 아닌 리스트의 갯수가 늘어난다.
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

# 값 비교
print('-------comparison value-------')
print(c == c[:3] + c[3:])       # 처음부터 3까지, 3부터 끝까지 더하면 총 합과 같다.
print(c == c[:])
print()

# Identity(id)
print('----------id----------')
temp = c
print(id(temp)!=id(c))          # 놀랍게도~~ 둘다 id값이 같다.
print()

# 리스트 수정, 삭제
print('-------modify list------')
c[0] = 4                        # 그냥 바꾸면 된다.
"""
아래 다음 4개의 차이점은 알아두자.
범위를 지정해서 리스트를 넣으면 원소가 들어가고
지정 인덱스에 리스트를 넣으면 리스트가 그대로 들어간다.
"""
print('c - ',c)
c[1:2] = ['a','b','c']          # 그냥 원소가 들어간다.
print('c - ', c)
c[1] = ['a','b','c']
print('c - ', c)
c[1:2] = [['a','b','c']]        # 이러면 리스트가 들어간다.
print('c - ', c)
c[1] = [['a','b','c']]
print('c - ', c)
print()

# 삭제
print('-------delete list-------')
c[1:3] = []
print('c - ', c)
del c[2]
print('c - ', c)
print()

# 리스트 함수
print('-------function of list-------')
a = [5,2,3,1,4]
print('a - ', a)
a.append(10)        # append 는 끝에 붙여주는 함수이다.
print('a - ', a)
a.sort()            # sort함수는 오름차순으로 정렬을 해준다.
print('a - ', a)
a.reverse()
print('a - ', a)    # reverse함수는 거꾸로 정렬해 준다.
print('a - ', a.index(3))   # index함수는 [index]의 값을 가져온다.
a.insert(2,7)       # insert함수 // 나는 2번 index에 7을 넣을거야 그리고 한칸씩 밀어
print('a - ', a)
a.remove(10)        # remove 함수는 특정 값을 제거한다.
print('a - ', a)
print('a - ', a.pop())  # pop 함수는 마지막 원소를 가져오고, 그걸 리스트에서 없앤다
print('a - ', a)
print('a - ', a.count(3))   # count 함수는 list안에 특정 값이 몇개가 중복되어 있는지,,
ex = [8,9]
a.extend(ex)        # extend 함수는 list 뒤에 list를 연결할 때 쓰인다.
print('a - ', a)
print()

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
    print(a)
