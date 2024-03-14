def summ(num):
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num = num // 10
    print('Сумма чисел', sum)
    return sum

def quantity(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    print('Количество цифр в числе:', count)
    return count

number = int(input('Введите число: '))

total = summ(number)
amount = quantity(number)

difference = total - amount
print('Разность суммы и количества цифр:', difference)

