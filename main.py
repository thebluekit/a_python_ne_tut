import random


print('1 - добавить строчные, 2 - добавить заглавные, 3 - добавить цифры')
inp = input()
print('Длина пароля')
line = int(input())

str_a = 'qwertyuiopasdfghjklzxcvbnm'
str_a1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
str_1 = '1234567890'
m_str = ''

if '1' in inp:
    m_str += str_a
if '2' in inp:
    m_str += str_a1
if '3' in inp:
    m_str += str_1

while line > 0:
    line -= 1
    print(random.choice(m_str), end='')



