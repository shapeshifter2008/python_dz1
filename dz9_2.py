class Road:
    def __init__(self, lenght, width, mass, height):
        self._lenght = lenght
        self._width = width
        self._mass = mass
        self._height = height

    def calc(self):
        return self._lenght * self._width * self._mass * self._height

road = Road(15, 1000, 5, 3)
print(road.calc())
