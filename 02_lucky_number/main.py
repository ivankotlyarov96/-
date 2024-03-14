import random
with open("out_file.txt", "w", encoding="utf8") as file:
    total_num = 0
    flag = True
    while flag:
        try:
            number = int(input('Введите число: '))
            num_random = random.randint(0, 13)

            if num_random == 6:
                flag = False
                raise RuntimeError("Вас постигла неудача")

            total_num += number
            file.write(f'{number}\n')

            if total_num >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                flag = False

        except Exception as exc:
            print(exc)



# TODO здесь писать код
