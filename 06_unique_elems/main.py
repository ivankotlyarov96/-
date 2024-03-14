first_list =[]
second_list = []
n = 0

for i in range(3):
    first_number = int(input(f'Введите {i + 1} число для первого списка:'))
    first_list.append(first_number)

for i in range(7):
    second_number = int(input(f'Введите {i + 1} число для второго списка:'))
    second_list.append(second_number)

first_list.extend(second_list)

for i in first_list:
    n = first_list.count(i)
    for _ in range(n - 1):
        first_list.remove(i)



print('Новый первый список с уникальными элементами:', first_list)








# TODO здесь писать код
