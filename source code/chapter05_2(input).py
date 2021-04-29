# Chpater 05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str) -> 입력은 알맞게 형변환 해주는 것이 중요하다.

# 예제1
#name = input('Enter your name : ')
#grade = input('Enter your grade : ')
#company = input('Enter your company name : ')

#print(name, grade, company)
#print()

# 예제2
#number = input('Enter number : ')
#name = input('Enter name : ')

#print('Type of number', type(number))
#print('Type of name', type(name))
#print()

# 예제3(계산)
#number1 = int(input('Enter first number : '))
#number2 = int(input('Enter second number : '))

#print('total number = ', number1 * number2)
#print()

# 예제4
#float_number = float(input("Enter a float number : "))
#print('input float : ', float_number)
#print('input type : ', type(float_number))
#print()

# 예제5
print('FirstNmae - {0}, LastName - {1}'.format(input('Enter first name : '), input("Enter Second name : ")))
