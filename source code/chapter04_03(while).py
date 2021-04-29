# Chpater04-3
# 파이썬 반복문
# while 실습

# while <expr>:
#     <statemanet(s)>

# 예제 1
n = 50
while n > 0:
    print(n)
    n = n-1

# 예제 2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())
print()

# 예제 3
# break, continue
n = 5
while n > 0:
    print(n)
    n -= 1
    if n == 2:
        break
print('Loop end')
print()

# 예제4
m = 5
while m > 0:
    m -= 1
    if(m == 2):
        continue
    print(m)
print('Loop end')
print()

# 예제5
i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
print()

# while - else 구문

# 예제 6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 4:
        break
else:
    print('else out')
print()

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'

i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')
print()

# 예제 8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
