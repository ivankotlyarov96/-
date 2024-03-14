
number = int(input('Введите число: '))
i = 1

while i <= number:
    i = i + 1
    if number % i == 0:
        print('Наименьший делитель, отличный от единицы:', i)
        break
