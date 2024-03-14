
with open("people.txt", "r", encoding='utf8') as file, open('error.log', "w", encoding='utf8') as log_file:

    count = 0
    count_line = 0

    for line in file:
        try:
            count_line += 1
            i_ine = line.rstrip()
            count += len(i_ine)

            if len(i_ine) < 3:
                raise RuntimeError('Длина {} строки меньше 3 символов'.format(count_line))

        except RuntimeError as exc:
            log_file.write(str(exc))

        except Exception as exc:
            log_file.write(str(exc))

    print('Общее кол-во символов в строках', count)






# TODO здесь писать код
