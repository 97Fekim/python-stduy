# Chpater03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))

# 이스케이프 문자 사용(\)
print('I\'m Boy')
print('a \t b')
print('a \"" b')

"""
참고 : Escape 코드

\n : 줄바꿈
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

escape_str1 = "Do you have a \"retror games?\"?"
print(escape_str1)

# 탭, 줄 바꿈
t_s1 = "Click\tStart!"
t_s2 = "New Line\nCheck"

print(t_s1)
print(t_s2)
print()

# Row String 출력
raw_s1 = r'D:\python\test'

print(raw_s1)   # 역슬래쉬(\)가 Escape로 쓰이지 않고 그대로 출력이 된다.

# 멀티라인 입력
multi_line = \
'''
kkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkkkk
kkkkkkkkkkkkkkkkkkk
'''
print(multi_line)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"
str_o5 = str_o1 * 3

print(str_o2 + str_o3)
print('y' in str_o1)    # 'y' 가 str_o1에 있니?
print('z' in str_o1)
print('P' not in str_o2)    # 'P' 가 str_o2에 없니?

# 문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1))
print(str(True),type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)
print("Capitalize: ", str_o1.capitalize())  # capitalize는 대문자로 바꿔주는 함수이다
print("endswith: ", str_o2.endswith("!"))   # endswith는 마지막이 parameter로 끝나는지
print("replace", str_o1.replace("thon","Good")) # replace는 좌 > 우 로 바꿔준다.
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' ')) # split은 매개변수를 기준으로 분류할 때 쓴다.

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # dir은 im_Str에서 사용할 수 있는 모든 들을 나열
                    # 그리고 ___iter___가 있는걸 보니 반복을 쓸 수 있나보다.
for i in im_str:    # 문자열은 시퀀스이기 때문에 슬라이스 처리를 할 수 있다.
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3])  # 3-1 즉 0 ~ 2까지 출력된다.
print(str_s1[5:11]) # 5~10 까지 출력된다.
print(str_s1[5:])   # 5부터 끝까지 출력된다.
print(str_s1[:len(str_s1)]) # 처음부터 str_s1의 끝까지 출력된다.
print(str_s1[1:9:2])    # 1부터 9까지 가져오는데 2칸씩 가져와라
print(str_s1[-5:])  # 끝 인덱스는 -1로도 표현 가능하다. 즉 -5번째는 뒤에서 5번째
print(str_s1[1:-2]) # 1부터 끝에서 2번째
print(str_s1[::2])  # 처음부터 끝까지 2칸 간격으로 출력해라
print(str_s1[::-1]) # 거꾸로 1개씩 다 출력해라

# 아스키 코드(또는 유니코드)
a__ = 'z'

print(ord(a__)) # a__(z)는 아스키코드에서 몇번이야!
print(chr(122)) # 아스키코드에서 122번은 z야!
