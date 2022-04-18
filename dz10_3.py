class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num//rows)])+'\n'+'*'*(self.num % rows)

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return 'Сумма клеток равна: '+str(self.num + other.num)

    def __sub__(self, other):
        return self.num - other.num if self.num - other.num > 0 else 'Клеток в первой меньше или равно второй'

    def __mul__(self, other):
        return 'Умножение клеток равно: '+str(self.num * other.num)

    def __truediv__(self, other):
        return 'Truediv' + str(round(self.num / other.num))

cell_1 = Cell(10)
cell_2 = Cell(34)

print(cell_1)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_2.make_order(5))
