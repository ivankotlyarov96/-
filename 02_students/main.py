from student import*

students = []

for i in range(10):
    print(f'{i +1} студент ')
    name = input('Введите имя: ')
    number = int(input('Введите номер группы: '))
    grade = list(map(int, input('Введите оценки через пробел: ').split()))
    students.append(Student(name, number, grade))

students_sorted = sorted(students, key=lambda student: student.sorted_students())

print(*students_sorted, sep='\n')

# TODO здесь писать код
