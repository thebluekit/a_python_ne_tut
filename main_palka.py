empty_li = []  # пустой список
filled_li = [1, 2, 3, 4, 5]  # заполненный список
filled_li.append(100500)  # добавление в список
print(filled_li[1])  # вывели конкретное число
print(filled_li)  # выводим все, что есть в этом списке

empty_tup = ()  # пустой кортеж
filled_tup = (1, 2, 3)  # заполненный кортеж
print(filled_tup[0])  # вывели конкретное число
print(filled_tup)  # выводим все, что есть в этом кортеже

empty_dict = {}  # пустой словарь
filled_dict = {"one": 1, "two": 2, "three": 3}  # заполненный словарь
print(filled_dict["one"])  # доступ по ключу


y = 12
z = 10

for x in range(z):
    pass
    print(filled_li)

while y > z:
    pass
    print(filled_tup)
    y -= 1

while True:
    pass
    print(filled_dict["one"])
    y += 1
    if y > z:
        break