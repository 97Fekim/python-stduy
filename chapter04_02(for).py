# Chpater 04-2
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10):     # 10번 반복, 0 ~ 9
    print('v1 is : ', v1)

for v2 in range(1,11):  # 10번 반복, 1 ~ 10
    print('v2 is : ', v2)

for v3 in range(1,11,2):
    print('v3 is : ', v3)   # 1 ~ 10까지 한칸씩 띄고

# 1 ~ 1000합 구하기
sum1 = 0
for v in range(1,1001):
    sum1 += v
print('sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))    # sum()이라는 함수가 따로 존재한다.
print('1 ~ 1000 sum of 4  : ', sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리) << 전부다 반복문을 사용 가능하다.
# iterable 리턴 함수 : range, reverse, enumerate, filter, map, zip

# 예제1
names = ['kim', 'park', 'cho', 'lee', 'choi', 'yoo']
for n in names:
    print('You are : ', n)

# 예제2
lotto_numbers = [11,19,21,28,36,37]
for n in lotto_numbers:
    print('current number : ', n)

# 예제3
word = 'Beautiful'
for s in word:
    print(s)

# 예제4
my_info = {
    'name' : 'lee',
    'age' : 22,
    'city' : 'seoul'
}
for k in my_info:
    print('key : ', my_info[k])  # 그냥 k 하면 key를 출력, [k]를 하면 value를 출력
print()

for v in my_info.values():  # values()함수를 이용 가능하다
    print('value : ', v)
print()

for key in my_info.keys():  # keys() 함수를 이용 가능하다.
    print('key : ', key)
print()

# 예제 5
name = 'FineAppLE'

for n in name:      # 대문자만 출력하기.(upper(), isupper() 이룔)
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

# break
numbers = [14,3,4,7,10,24,17,2,33,16,34,36,38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)
print()

# continue
lt = ["1", 2, 5, True, 4, 3, complex(4)]

for v in lt:
    if type(v) is bool:      # 자료형을 비교할 때는 is, is not 을 쓴다.
        continue            # continue를 만나면, 아래 구문은 실행하지 않고, 스킵한다.
    print("current type : ", v , type(v))
print()

# for - else
numbers = [14,3,4,7,10,24,17,2,33,16,34,24,38]

for num in numbers:     # for-else문은 for문을 다 돌고 나면 else문이 실행 된다.
    if num == 24:       # for문 속 if문에 의해 break가 걸릴 경우 else 구문은 실행되지 않는다.
        print("Found : 24")
        break
else:
    print("Not Found : 24")
print()

# 구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i * j), end='')
    print()
print()

numbers = [14,3,4,7,10,24,17,2,33,16,34,36,38]
# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))      # 리버스만 하면, 순서만 바뀌어 저장된다.
print('list', list(reversed(name2)))    # 리버스 후 형변환해서 가져다 쓸 수 있다.
print('Tuple', tuple(reversed(name2)))  # 튜플로도 형변환 가능하다.
print('Set', set(reversed(name2)))      # set으로 형변환하면 순서가 없어진다.
