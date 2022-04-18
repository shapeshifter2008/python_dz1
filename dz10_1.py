class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line1) != len(line_2):
                    return 'Ошибка формы'

                summ_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summ_line)) + '\n'
        else:
            return 'Ошибка формы'

        return answer

matrix = Matrix([[31,22], [37,43], [51,86], [3,5,32], [2,4,6], [-1, 64, -8]])
print(matrix)