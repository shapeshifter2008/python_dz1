class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 1: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 2: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки 3: {self.title}')

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()