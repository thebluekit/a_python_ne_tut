a = '=================================='

empty_li = []  # пустой список
filled_li = [1, 2, 3, 4, 5]  # заполненный список
filled_li.append(6)  # добавление в список
print(filled_li[1])  # вывели конкретное число
print(filled_li)  # выводим все, что есть в этом списке

empty_tup = ()  # пустой кортеж
filled_tup = (1, 2, 3)  # заполненный кортеж
print(filled_tup[0])  # вывели конкретное число
print(filled_tup)  # выводим все, что есть в этом кортеже

empty_dict = {}  # пустой словарь
filled_dict = {"1": 1, "2": 2, "3": 3}  # заполненный словарь
print(filled_dict["1"])  # доступ по ключу

y = 12
z = 10
for x in range(z):
    pass

while y < z:
    pass

while True:
    pass
    if y > z:
        break

print()
print(a)
print()

for t in range(6):
    print(filled_li[t], " ", end='')

print()

for t in range(3):
    print(filled_tup[t], " ", end='')

print()

for t in range(3):
    t = str(t)
    print(filled_dict["t"], " ", end='')
    t = int(t)