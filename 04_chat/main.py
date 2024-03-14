user = input('Введите имя пользователя: ')

while True:
    print('Введите 1 чтобы увидеть все сообщения чата  или 2 чтобы напсиать нвое сообщение в чат ')
    count = input('Введите 1 или 2: ')
    if count == '1':
        try:
            with open('chat.txt', "r", encoding='utf8') as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Ошибка, такого файла нет или список сообщений пуст")
    elif count == '2':
        new_message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf8') as file:
            file.write('{0}: {1}\n'.format(user, new_message))
    else:
        print('Неправильная команда введите 1 или 2!')






# TODO здесь писать код
