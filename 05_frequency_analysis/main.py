def frequency_dictionary(file, num_len):
    dict_char = {}
    for line in file:
        for i_line in line:
            if i_line.isalpha():
                if i_line not in dict_char:
                    dict_char[i_line] = 0
                dict_char[i_line] += 1

    final_dict = {}
    for char, freg in dict_char.items():
        final_dict[char] = round(freg / num_len, 3)
    return final_dict

def sorted_frequency(i_dict):
    sorted_values = sorted(i_dict.values(), reverse=True)

    sorted_dict = {}
    for i_value in sorted_values:
        for i_key in i_dict.keys():
            if i_dict[i_key] == i_value:
                sorted_dict[i_key] = i_dict[i_key]
    print(sorted_dict)

    return sorted_dict






file = open("text.txt", 'r', encoding="utf8").read()

file_first = file.lower()
len_num = float(len(file_first))

dict_freg = frequency_dictionary(file_first, len_num)
final_dict = sorted_frequency(dict_freg)

file_freg = open('analysis.txt', "w", encoding="utf8")

for key, value in final_dict.items():
    line = str(key) + " " + str(value)
    file_freg.write(f"{line}" + '\n')
file_freg.close()












# TODO здесь писать код
