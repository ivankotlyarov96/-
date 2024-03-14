list_first = []
list_second = []

begin_first = int(input('Введите начало см в первом классе: '))
end_first = int(input('Введите нконец см в первом классе: '))
step_first = int(input('Введите шаг в первом классе: '))

begin_second = int(input('Введите начало см во втором классе: '))
end_second = int(input('Введите нконец см во втором классе: '))
step_second = int(input('Введите шаг во втором классе: '))

list_first = list(range(begin_first, end_first + 1, step_first))

list_second = list(range(begin_first, end_first + 1, step_first))

for i in list_second:
    list_first.append(i)

list_first.sort()

print('Отсортированный список учеников:', list_first)



# TODO здесь писать код
