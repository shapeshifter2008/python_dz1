class Car:
    def __init__(self, speed, color, name, is_pilice):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_pilice = is_pilice

    def go(self):
        print(f'{self.name} Go!')

    def stop(self):
        print(f'{self.name} Stop!')

    def turn(self, direction):
        print(f'{self.name} is turn to {direction}')

    def show_speed(self):
        print(f'Speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning! Speed limit 60!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Warning! Speed limit 40!')

class PoliceCar(Car):
    pass

sport_car = SportCar(210, 'Yellow', 'Lambo', False)
town_car = TownCar(120, 'Green', 'Lada', False)
work_car = WorkCar(100, 'Black', 'Lada', False)
police_car = PoliceCar(900, 'Blue', 'Bentley', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()

sport_car.turn('left')