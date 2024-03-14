from father_and_keeds import*

def data_keeds():
    age_keed = int(input('Введите возраст ребенка: '))
    if age_keed > (Parent.age - 16):
        print('Ошибка возраст ребенка должен быть минимум меньше на 16 лет возраста родителя')
        age_keed = int(input('Введите возраст ребенка: '))
    name = input('Введите имя ребенка ')
    return name, age_keed


list_keeds = []

name, age = data_keeds()
keeds_1 = Keeds(name, age)
name_1, age_1 = data_keeds()
keeds_2 = Keeds(name_1, age_1)

list_keeds.append(keeds_1)
list_keeds.append(keeds_2)

parent_1 = Parent('Tom', list_keeds)

parent_1.calm_keed()
parent_1.feed_keed()

parent_1.info_print()

# здесь немного запутался в метода кормления ребенка и успокоения я понимаю что сделал немного не так
# и пойму как правильно, также не пойму как правильно сделать вывод спика обьекта а не его местоположение и информации о нем


# TODO здесь писать код
