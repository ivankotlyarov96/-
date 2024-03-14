class Humans:
    name = ""
    degree_satiety = 50
    house = {"fridge": 50, "money": 0}
    day = 0

    def __init__(self, name):
        self.name = name

    def there_is(self):
        self.degree_satiety += 15
        self.house["fridge"] -= 5
        print(f'Поел, сытость: {self.degree_satiety}, еды осталось { self.house["fridge"]}')
    def work_is(self):
        self.degree_satiety -= 5
        self.house["money"] += 50
        print(f'Поработали, сытость: {self.degree_satiety} денег стало: {self.house["money"]}')

    def play_is(self):
        self.degree_satiety -= 5
        print(f'Играем, сытость: {self.degree_satiety}')

    def go_to_the_store(self):
        self.house["fridge"] += 15
        self.house["money"] -= 10
        print(f'Пошли в магазин за едой, еды стало: {self.house["fridge"]} денег осталось: {self.house["money"]}')

    def live_day(self):
        self.day += 1
        print(f'Прошел еще один день. всего прошло дней с начала эксперемента: {self.day}')

