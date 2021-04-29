# Chapter06-2
# 파이썬 모듈
# Modlue : 함수, 변수, 클래스 등 파이썬 구성요소 등을 모아놓은 파일.

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def dived(x,y):
    return x / y

def power(x,y):
    return x ** y

#print('-' * 15)
#print('called! inner!')
#print(add(5,5))
#print(subtract(15,5))
#print(multiply(5,5))
#print(dived(10,2))
#print(power(5,3))
#print('-' * 15)

# __name__ 사용
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(dived(10,2))
    print(power(5,3))
    print('-' * 15)
