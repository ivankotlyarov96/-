
class Matrix():
    def __init__(self, row, colum):
        self.row = row
        self.colum = colum
        self.data = [[0] * self.colum for _ in range(self.row)]

    def add(self, first):
        list_1 = []
        list_2 = []
        for i in range(len(first.data)):
            for j in range(len(first.data[i])):
                list_1.append(self.data[i][j] + first.data[i][j])
            list_2.append(list_1)
            list_1 = []
        for x in list_2:
            print(x)
        print(' ')
    def subtract(self, first):
        list_1 = []
        list_2 = []
        for i in range(len(first.data)):
            for j in range(len(first.data[i])):
                list_1.append(self.data[i][j] - first.data[i][j])
            list_2.append(list_1)
            list_1 = []
        for x in list_2:
            print(x)
        print(' ')
    def __str__(self):
        res = ''
        for i in self.data:
            s = ''
            for j in i:
                s += str(j) + ' '
            res += s + '\n'
        return res

    def multiply(self, other):
        rows_a = len(self.data)
        cols_a = len(self.data[0])
        rows_b = len(other.data)
        cols_b = len(other.data[0])

        result = [[0 for row in range(cols_b)] for col in range(rows_a)]

        for s in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[s][j] += self.data[s][k] * other.data[k][j]
        for i in result:
            print(i)
        print(' ')

    def transpose(self):
        transp = [[0 for j in range(len(self.data))] for i in range(len(self.data[0]))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                transp[j][i] = self.data[i][j]
        for x in transp:
            print(x)
        print(' ')









m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]
print('Матрица 1:')
print(m1)

print('Матрица 2:')
print(m2)

print('Сложение матриц:')
m1.add(m2)

print('Вычитание матриц:')
m1.subtract(m2)

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print('Умножение матриц:')
m1.multiply(m3)

print('Транспортирование матрицы 1:')
m1.transpose()

