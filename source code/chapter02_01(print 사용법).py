# chater02-1
# 파이썬 완전 기초
# printf 사용법
print('python Start!')
print("python start!")
print('''python start''')
print("""python start""")

# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep = '')
print('010','7777','1234',sep = '-')
print('python', 'google.com', sep='@')

# end 옵션
print('welcome to', end=' ')
print('IT news',end = ' ')
print('web site')

# file 옵션
import sys

print('Learn Python', file = sys.stdout)
print()

# format 사용(d:정수, s:문자열, f:실수) // 외워야 함.
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one', 'two'))
print('{0},{2},{3},{1}'.format('one', 'four', 'two','three'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f
print('%1.12f' % (3.142312414))
print('{:f}'.format(3.142312414))

print('%06.2f' % (3.14159212121212))
print('{:06}')
print()
