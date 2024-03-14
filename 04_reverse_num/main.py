def reverse(num):
    first = str(num).split(".")
    first[0] = "".join(reversed(first[0]))
    first[1] = "".join(reversed(first[1]))
    return float(first[0] + '.' + first[1])



first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

first_rever = reverse(first_number)
second_rever = reverse(second_number)

print('Первое число наоборот: ', first_rever)
print('Второе число наоборот: ', second_rever)
print('Сумма: ', first_rever + second_rever)


