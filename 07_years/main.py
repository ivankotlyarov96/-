def same_years(num1, num2):
    for i in range(num1, num2 + 1):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if a == b == c or b == c == d or c == d == a or a == b == d:
            print(i)


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
print('Годы от 1900 до 2100 с тремя одинаковыми цифрами:')

same_years(first_year, second_year)


