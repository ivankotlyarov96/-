a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
count_5 = 0
count_3 = 0

for i in b:
    a.append(i)

for i in a:
    if i == 5:
        count_5 += 1

while 5 in a:
    a.remove(5)

a.extend(c)

count_3 = a.count(3)

print('Кол-во цифр 5 при первом объединении:', count_5)
print('Кол-во цифр 3 при втором объединении:', count_3)
print('Итоговый список:', a)


