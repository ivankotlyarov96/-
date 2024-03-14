num_friends = int(input('Кол-во друзей: '))
note = int(input('Долговых расписок: '))
money_list =[]

for i in range(num_friends):
    money_list.append(0)

for i in range(note):
    print(f'{i + 1} - я расписка')
    to_whom = int(input('Кому? '))
    from_whom = int(input('От кого? '))
    how_many = int(input('Сколько? '))
    money_list[from_whom - 1] -= how_many
    money_list[to_whom - 1] += how_many

print('\nБаланс друзей: ')
for i in range(len(money_list)):
    print(f'{i + 1} : {money_list[i]}')




# TODO здесь писать код
