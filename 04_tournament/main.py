
file = open("first_tour.txt", "r", encoding="utf8")
count = int(file.readline())
new_list = []

for line in file:
    new_line = line.split()
    if int(new_line[2]) > count:
        new_list.append(new_line)

file.close()
new_list.sort(key=lambda a: int(a[2]))
new_list.reverse()

count = str(len(new_list))
n = 1
final_list = []
print(new_list)

for i in new_list:
    name = str(i[0][0] + '.')
    family_and_num = str(n) + ')' + " " + name + " " + i[1] + ' ' + i[2]
    final_list.append(family_and_num)
    n += 1



file_second = open("second_tour.txt", 'w', encoding="utf8")
file_second.write(str(count) + '\n')
result = "\n".join(final_list)
file_second.write(result)
file_second.close()







# TODO здесь писать код
