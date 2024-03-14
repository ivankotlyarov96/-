import os
def file_dir(path_total, list):
    for i_elem in os.listdir(path_total):
        path = os.path.join(path_total, i_elem)
        if os.path.isfile(path):
            list[0] += 1
            list[2] += os.path.getsize(path)
        elif os.path.isdir(path):
            list[1] += 1
            file_dir(path, list)
    return


way = input('Введите путь: ')
list = [0, 0, 0]

path_to = os.path.join(way)

file_dir(path_to, list)

print('Размер каталога (в Кбайтах):', round((list[2] / 1024), 2))
print('Количество подкаталогов:', list[1])
print('Количество файлов:', list[0])

# TODO здесь писать код
