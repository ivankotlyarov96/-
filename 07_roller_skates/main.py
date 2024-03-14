skate_size = []
foot_size = []
count = 0

numbers_skat = int(input('Введите кол-во коньков: '))

for i in range(numbers_skat):
    size = int(input(f'Размер {i + 1} пары: '))
    skate_size.append(size)

numbers_human = int(input('Введите кол-во людей: '))

for i in range(numbers_human):
    size = int(input(f'Размер ноги {i + 1} человека: '))
    foot_size.append(size)

foot_size.sort()
skate_size.sort()

for i in foot_size:
    for j in skate_size:
        if j >= i:
            skate_size.remove(j)
            count += 1

print('Наибольшее кол-во людей, которые могут взять ролики: ', count)

# TODO здесь писать код
