guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке ', len(guests), 'человек', guests)
    action = input('Гость пришел или ушел? ')
    if action == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет, ', name)
            guests.append(name)
        else:
            print('Прости,', name, 'но, мест нет')
    if action == 'ушел':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока,', name, '!')
    if action == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break






# TODO здесь писать код
