from warrior import *

warrior_1 = Warrior('Alex')
warrior_2 = Warrior('Rain')

while True:
    question = input(f'Какой воин атакует ? если {warrior_1.name} введите 1, если {warrior_2.name} введите 2: ')
    if question == str(1):
        print(f'{warrior_1.name} атакует {warrior_2.name}')
        warrior_2.hit()
        print(f'у {warrior_2.name} осталось {warrior_2.heath} здоровья')
    elif question == str(2):
        print(f'{warrior_2.name} атакует {warrior_1.name}')
        warrior_1.hit()
        print(f'у {warrior_1.name} осталось {warrior_1.heath} здоровья')

    if warrior_1.heath == 0:
        print(f'Игра окончена. {warrior_2.name} выиграл')
        break
    elif warrior_2.heath == 0:
        print(f'Игра окончена. {warrior_1.name} выиграл')
        break



# TODO здесь писать код
