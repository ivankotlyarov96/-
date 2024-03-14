human_list = []
numbers_human = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
out = 0

print(f'Значит, выбывает каждый {number} человек')

for i in range(1, numbers_human + 1):
    human_list.append(i)

for _ in range(numbers_human - 1):
    print('\nТекущий кург людей ', human_list)
    start_count = out % len(human_list)
    out = (start_count + number - 1) % len(human_list)
    print('Начало счета с номера: ', human_list[start_count])
    print('Выбывает человек под номером ', human_list[out])
    human_list.remove(human_list[out])

print('\nОстался человек с номером ', human_list)



# TODO здесь писать код
