class Student:
    def __init__(self, name, number, grade):
        self.name = name
        self.number = number
        self.grade = grade

    def sorted_students(self):
        return (sum(self.grade)) / len(self.grade)

    def __str__(self):
        return self.name