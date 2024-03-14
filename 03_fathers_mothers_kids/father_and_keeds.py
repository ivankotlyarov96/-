class Parent:
    age = 44
    def __init__(self, name, list_keeds):
        self.name = name
        self.list_keeds = list_keeds

    def info_print(self):
        print(f'Родитель - Имя: {self.name}\n Возраст: {self.age}\n Список детей: {self.list_keeds}\n')

    def calm_keed(self):
        print('Ребенок накормлен. ')
        keed_calm = True

    def feed_keed(self):
        print('Ребенок успокоен.')
        keed_feed = True

    def __str__(self):
        return self.list_keeds
class Keeds:
    keed_calm = False
    keed_feed = False

    def __init__(self, keed_name, age_keed):
        self.keed_name = keed_name
        self.age_keed = age_keed

    def __str__(self):
        return self.keed_name

