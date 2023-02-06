#1
for index in range(3):
   name = input('Как вас завут :')

#2
'''
name = input('Как вас завут :')

for i in range(3):





'''    

#3
'''
name = input('Как вас завут :')
for i in name:
    print(i, end=' ')
'''
#4
'''
name = input('Как вас завут :')
for index in range(name):
    number = input('Как ваш номер: ')
    name = input('Как вас завут :')
    print(number)
    for i in name:
       print(i)
'''

#6
'''
a  = int(input('a: '))
if a > 0 and a < 50:
         for i in range(50,a-1,-1):
            print(i, end=' ')
else:
    print('Ошибка')
'''
#7
'''
name = input('Как вас завут : ')
number = input('Как ваш номер: ')

if len(number) > 10:
    for index in name:
        print(name)
else:
    for index in range(3):
         print('Слишком высокое')
'''
#5
'''
N = int(input('N: '))
if N >= 1 and N <= 12:
    for i in range(1,11):
        print(N,'x',i, '=' ,N*i)
else:
    print('Ошибка')
'''
 #7-2
'''
name = input('Как вас завут : ')
number = int(input('Как ваш номер: '))
if number < 10:
    for i in range(number):
        print(name)
else:
    for index in range(3):
         print('Слишком высокое')
'''
#8
'''total = 0
for i in range(5):
    a = int(input('a: '))
    q = input('Хотите ли вы включить это число: ')
    if q == 'да':
        total += 1
print(total)        '''
