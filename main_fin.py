import random


print('1 - добавить строчные, 2 - добавить заглавные, 3 - добавить цифры')
inp = input()
print('Длина пароля')
line = int(input())

str_a = 'qwertyuiopasdfghjklzxcvbnm'
str_a1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
str_1 = '1234567890'

while line > 0:
    line -= 1
    m_inp = random.choice(inp)
    if m_inp == '1':
        print(random.choice(str_a), end='')
    elif m_inp == '2':
        print(random.choice(str_a1), end='')
    elif m_inp == '3':
        print(random.choice(str_1), end='')


