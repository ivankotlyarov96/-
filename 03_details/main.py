shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
quantity = 0
price = 0

for i in shop:
        if detail == i[0]:
                quantity += 1

for i in shop:
        if i[0] == detail:
                price += i[1]

print('Кол-во деталей —', quantity)
print('Общая стоимость-', price)
# TODO здесь писать  код
