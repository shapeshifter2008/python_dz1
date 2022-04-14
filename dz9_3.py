class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def calc(self):
        return self._lenght * self._width * self._mass * self._height

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}: {self.position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position('Nikita', 'Petrov', 'junior', {"wage": 15000, "bonus": 30000})
print(position.get_full_name())
print(position.get_total_income())
