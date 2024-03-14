from humans import *
import random
def life_of_play(human):
    while True:
        number = random.randint(1, 6)
        if human.day == 365:
            print(f'Эксперемент завершен удачно! {human.name} выжил')
            break
        if human.degree_satiety > 0:
            print(f'Эксперемнт не удался ! {human.name} умер от голода.')
            break
        if human.degree_satiety < 20 or number == 2:
            human.there_is()
        elif human.house["fridge"] < 10:
            human.go_to_the_store()
        elif human.house['money'] < 50 or number == 1:
            human.work_is()
        else:
            human.play_is()
        human.live_day()


human_1 = Humans('Tom')
human_2 = Humans('Bob')

life_of_play(human_1)
life_of_play(human_2)

#вроде сделал все правильно но чего то не учел, и почему print в методах не отоброжается в консоли?
# TODO здесь писать код
