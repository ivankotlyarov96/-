def is_palindrome(num_list):
    rever_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        rever_list.append(num_list[i_num])
    if num_list == rever_list:
        return True
    else:
        return False


numbers = int(input('Кол-во чисел:'))
nums = []
new_nums = []
answer = []

for i in range(numbers):
    number = int(input('Число: '))
    nums.append(number)

for i_nums in range(0, len(nums)):
    for j_nums in range(i_nums, len(nums)):
        new_nums.append(nums[j_nums])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(i_answer)
        answer.reverse()
        break
    new_nums = []

print('Последовательность:', nums)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)



# TODO здесь писать код
